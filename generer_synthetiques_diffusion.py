"""Génère des défauts synthétiques avec Stable Diffusion Inpainting.

Le générateur n'utilise que data/<categorie>/train/good. Les masques de défaut
sont procéduraux : aucune image, aucun masque ni métadonnée du split test n'est
utilisé pour la génération.
"""

from __future__ import annotations

import argparse
import json
import random
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import torch
from PIL import Image, ImageDraw, ImageFilter
from tqdm import tqdm

# ===== Constantes =====
SEED = 42
CATEGORIES = ("bottle", "cable", "transistor")
N_PAR_CATEGORIE = 120
TAILLE_SORTIE = 256
TAILLE_DIFFUSION = 512
BATCH_SIZE = 4
NUM_STEPS = 25
GUIDANCE_SCALE = 7.0
MARGE_MASQUE = 5
ECART_MIN = 5.0
MODEL_ID = "stable-diffusion-v1-5/stable-diffusion-inpainting"
DATA_DIR = Path("./data")
SYNTH_DIR = Path("./synthetiques")
FIGURES_DIR = Path("./figures")
LOG_PATH = SYNTH_DIR / "LOG_diffusion.txt"
PROMPT_NEGATIF = (
    "cartoon, illustration, drawing, blurry, low quality, text, watermark, "
    "multiple objects, duplicate, deformed object, unrealistic lighting"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n-par-categorie", type=int, default=N_PAR_CATEGORIE)
    parser.add_argument("--categories", nargs="+", default=list(CATEGORIES))
    parser.add_argument("--output-dir", type=Path, default=SYNTH_DIR)
    parser.add_argument("--device", choices=("auto", "cuda", "cpu"), default="auto")
    parser.add_argument("--keep-existing", action="store_true")
    return parser.parse_args()


def choisir_device(demande: str) -> torch.device:
    if demande == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("CUDA demandé mais indisponible")
    if demande == "cpu":
        return torch.device("cpu")
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def charger_pipeline(device: torch.device):
    from diffusers import StableDiffusionInpaintPipeline

    dtype = torch.float16 if device.type == "cuda" else torch.float32
    pipe = StableDiffusionInpaintPipeline.from_pretrained(
        MODEL_ID,
        dtype=dtype,
        variant="fp16" if dtype == torch.float16 else None,
        safety_checker=None,
        requires_safety_checker=False,
    )
    pipe = pipe.to(device)
    pipe.set_progress_bar_config(disable=True)
    if device.type == "cuda":
        pipe.enable_attention_slicing()
        torch.backends.cuda.matmul.allow_tf32 = True
        torch.backends.cudnn.allow_tf32 = True
    return pipe


DEFECTS = {
    "bottle": [
        {
            "nom": "fissure",
            "forme": "fissure",
            "prompt": (
                "a realistic close-up photograph of a glass bottle with a long deep "
                "crack, sharp broken glass edges, industrial inspection, high detail"
            ),
        },
        {
            "nom": "contamination",
            "forme": "tache",
            "prompt": (
                "a realistic glass bottle surface with dark contamination stains, "
                "dirt spots and oily residue, macro photography, industrial defect"
            ),
        },
        {
            "nom": "eclat",
            "forme": "eclat",
            "prompt": (
                "a realistic glass bottle rim with a chipped edge and a missing glass "
                "fragment, sharp broken glass, industrial inspection photograph"
            ),
        },
    ],
    "cable": [
        {
            "nom": "coupure",
            "forme": "coupure",
            "prompt": (
                "a realistic macro photograph of a black electrical cable with a deep "
                "cut, torn rubber insulation and exposed copper wires, industrial defect"
            ),
        },
        {
            "nom": "isolant_arrache",
            "forme": "erosion",
            "prompt": (
                "a realistic macro photograph of a damaged black cable with peeled "
                "rubber insulation exposing metal, worn and torn material, industrial defect"
            ),
        },
        {
            "nom": "cable_deforme",
            "forme": "deformation",
            "prompt": (
                "a realistic macro photograph of a bent and pinched black electrical "
                "cable with deformed rubber insulation, industrial inspection"
            ),
        },
    ],
    "transistor": [
        {
            "nom": "boitier_endommage",
            "forme": "tache",
            "prompt": (
                "a realistic macro photograph of a damaged black electronic transistor "
                "case with a crack and chipped plastic, industrial defect"
            ),
        },
        {
            "nom": "broche_tordue",
            "forme": "deformation",
            "prompt": (
                "a realistic macro photograph of a black electronic transistor with a "
                "bent silver metal lead, deformed component, industrial defect"
            ),
        },
        {
            "nom": "broche_coupee",
            "forme": "coupure",
            "prompt": (
                "a realistic macro photograph of a transistor component with a cut "
                "silver metal lead, broken electronic component, industrial inspection"
            ),
        },
    ],
}


def charger_images_normales(categorie: str) -> list[Path]:
    images = sorted((DATA_DIR / categorie / "train" / "good").glob("*.png"))
    if not images:
        raise FileNotFoundError(f"Aucune image normale pour {categorie}")
    return images


def masque_objet(image: Image.Image) -> np.ndarray:
    arr = np.asarray(image, dtype=np.float32)
    bord = np.concatenate(
        [arr[:12].reshape(-1, 3), arr[-12:].reshape(-1, 3),
         arr[:, :12].reshape(-1, 3), arr[:, -12:].reshape(-1, 3)]
    )
    fond = np.median(bord, axis=0)
    distance = np.linalg.norm(arr - fond, axis=-1)
    seuil = max(10.0, float(np.percentile(distance, 60)))
    masque = Image.fromarray(((distance > seuil) * 255).astype(np.uint8), "L")
    masque = masque.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.MinFilter(5))
    return np.asarray(masque) > 127


def point_objet(rng: np.random.Generator, objet: np.ndarray) -> tuple[int, int]:
    ys, xs = np.where(objet[30:-30, 30:-30])
    if len(ys) == 0:
        return int(rng.integers(150, 362)), int(rng.integers(150, 362))
    i = int(rng.integers(0, len(ys)))
    return int(xs[i] + 30), int(ys[i] + 30)


def dessiner_forme(draw: ImageDraw.ImageDraw, rng, forme, centre):
    x, y = centre
    if forme == "fissure":
        points = [(x, y)]
        angle = rng.uniform(0, 2 * np.pi)
        for _ in range(int(rng.integers(4, 9))):
            angle += rng.uniform(-0.7, 0.7)
            longueur = rng.uniform(12, 28)
            points.append((points[-1][0] + longueur * np.cos(angle),
                           points[-1][1] + longueur * np.sin(angle)))
        draw.line(points, fill=255, width=int(rng.integers(2, 5)), joint="curve")
    elif forme == "tache":
        for _ in range(int(rng.integers(4, 9))):
            cx = x + rng.normal(0, 22)
            cy = y + rng.normal(0, 22)
            r = rng.uniform(3, 13)
            draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=255)
    elif forme == "eclat":
        angles = np.sort(rng.uniform(0, 2 * np.pi, 7))
        rayons = rng.uniform(10, 28, 7)
        points = [(x + r * np.cos(a), y + r * np.sin(a)) for a, r in zip(angles, rayons)]
        draw.polygon(points, fill=255)
    elif forme == "coupure":
        angle = rng.uniform(0, np.pi)
        dx, dy = np.cos(angle) * rng.uniform(30, 55), np.sin(angle) * rng.uniform(30, 55)
        largeur = int(rng.integers(9, 18))
        draw.line([(x - dx, y - dy), (x + dx, y + dy)], fill=255, width=largeur)
    elif forme == "erosion":
        angles = np.sort(rng.uniform(0, 2 * np.pi, 8))
        rayons = rng.uniform(18, 45, 8)
        points = [(x + r * np.cos(a), y + r * np.sin(a)) for a, r in zip(angles, rayons)]
        draw.polygon(points, fill=255)
    elif forme == "deformation":
        points = [(x + i * 16, y + rng.normal(0, 6)) for i in range(-3, 4)]
        draw.line(points, fill=255, width=int(rng.integers(18, 32)), joint="curve")


def creer_masque_procedural(image: Image.Image, forme: str, rng) -> Image.Image:
    objet = masque_objet(image)
    centre = point_objet(rng, objet)
    for _ in range(8):
        masque = Image.new("L", image.size, 0)
        dessiner_forme(ImageDraw.Draw(masque), rng, forme, centre)
        if 0.002 < np.count_nonzero(np.asarray(masque)) / (image.width * image.height) < 0.15:
            return masque.filter(ImageFilter.MaxFilter(2 * MARGE_MASQUE + 1))
    return masque


def charger_base(chemin: Path, rng) -> Image.Image:
    image = Image.open(chemin).convert("RGB").resize(
        (TAILLE_DIFFUSION, TAILLE_DIFFUSION), Image.Resampling.LANCZOS
    )
    if rng.random() < 0.5:
        image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    return image


def ecart_moyen(ancienne: Image.Image, nouvelle: Image.Image, masque: Image.Image) -> float:
    a = np.asarray(ancienne, dtype=np.float32)
    b = np.asarray(nouvelle, dtype=np.float32)
    m = np.asarray(masque) > 127
    return float(np.abs(a[m] - b[m]).mean()) if m.any() else 0.0


def generer_lot(pipe, bases, masques, prompts, device, seed):
    generateur = torch.Generator(device=device.type).manual_seed(seed)
    return pipe(
        prompt=prompts,
        negative_prompt=[PROMPT_NEGATIF] * len(prompts),
        image=bases,
        mask_image=masques,
        height=TAILLE_DIFFUSION,
        width=TAILLE_DIFFUSION,
        num_inference_steps=NUM_STEPS,
        guidance_scale=GUIDANCE_SCALE,
        generator=generateur,
    ).images


def generer_categorie(pipe, categorie, n_images, output_dir, device, seed_base):
    rng = np.random.default_rng(seed_base + CATEGORIES.index(categorie))
    normales = charger_images_normales(categorie)
    dossier = output_dir / categorie
    dossier.mkdir(parents=True, exist_ok=True)
    faibles = 0
    for debut in tqdm(range(0, n_images, BATCH_SIZE), desc=f"Diffusion {categorie}"):
        taille = min(BATCH_SIZE, n_images - debut)
        bases, masques, prompts = [], [], []
        for i in range(debut, debut + taille):
            defaut = DEFECTS[categorie][i % len(DEFECTS[categorie])]
            base = charger_base(normales[int(rng.integers(0, len(normales)))], rng)
            bases.append(base)
            masques.append(creer_masque_procedural(base, defaut["forme"], rng))
            prompts.append(defaut["prompt"])
        images = generer_lot(pipe, bases, masques, prompts, device, seed_base + debut)
        for i, (image, base, masque) in enumerate(zip(images, bases, masques), start=debut):
            if ecart_moyen(base, image, masque) < ECART_MIN:
                genere = generer_lot(
                    pipe, [base], [masque], [prompts[i - debut]], device,
                    seed_base + i + 100_000,
                )[0]
                if ecart_moyen(base, genere, masque) > ecart_moyen(base, image, masque):
                    image = genere
                faibles += 1
            image.resize((TAILLE_SORTIE, TAILLE_SORTIE), Image.Resampling.LANCZOS).save(
                dossier / f"synth_{i:03d}.png"
            )
    return len(list(dossier.glob("synth_*.png"))), faibles


def sauvegarder_grille(output_dir: Path, categories, n_col: int = 5) -> Path:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(len(categories), n_col, figsize=(n_col * 2.3, len(categories) * 2.4))
    axes = np.atleast_2d(axes)
    for ligne, categorie in enumerate(categories):
        images = sorted((output_dir / categorie).glob("synth_*.png"))[:n_col]
        axes[ligne, 0].set_ylabel(categorie, fontsize=11)
        for col in range(n_col):
            axes[ligne, col].axis("off")
            if col < len(images):
                axes[ligne, col].imshow(Image.open(images[col]).convert("RGB"))
    fig.suptitle("Défauts synthétiques générés par Stable Diffusion Inpainting", fontsize=13)
    fig.tight_layout()
    chemin = FIGURES_DIR / "fig_synthetiques_diffusion_exemples.png"
    fig.savefig(chemin, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return chemin


def ecrire_log(compteurs, output_dir, device, faibles, n_images):
    lignes = [
        "=== LOG génération de défauts synthétiques par diffusion — IND-3 ===",
        f"Date : {datetime.now().isoformat()}",
        f"Méthode : Stable Diffusion Inpainting préentraîné (sans fine-tuning)",
        f"Modèle : {MODEL_ID}",
        f"Device : {device}",
        f"Seed globale : {SEED}",
        f"Images par catégorie : {n_images}",
        f"Taille de diffusion : {TAILLE_DIFFUSION}x{TAILLE_DIFFUSION}",
        f"Taille sauvegardée : {TAILLE_SORTIE}x{TAILLE_SORTIE}",
        f"Pas d'inférence : {NUM_STEPS}",
        f"Guidance scale : {GUIDANCE_SCALE}",
        f"Batch size : {BATCH_SIZE}",
        f"Marge de dilatation du masque : {MARGE_MASQUE} px",
        f"Conditionnement : images train/good + masques procéduraux",
        "Données test utilisées pour la génération : NON",
        f"Prompt négatif : {PROMPT_NEGATIF}",
        "",
        "Défauts et prompts par catégorie :",
        json.dumps(DEFECTS, ensure_ascii=False, indent=2),
        "",
        "Images générées par catégorie :",
    ]
    lignes += [f"  {cat} : {n}" for cat, n in compteurs.items()]
    lignes += [
        f"  Images avec faible écart initial (retentées) : {faibles}",
        f"  TOTAL : {sum(compteurs.values())}",
        "",
    ]
    (output_dir / LOG_PATH.name).write_text("\n".join(lignes), encoding="utf-8")


def main():
    args = parse_args()
    random.seed(SEED)
    np.random.seed(SEED)
    torch.manual_seed(SEED)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(SEED)
    device = choisir_device(args.device)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pipe = charger_pipeline(device)

    compteurs, faibles = {}, 0
    for categorie in args.categories:
        dossier = args.output_dir / categorie
        dossier.mkdir(parents=True, exist_ok=True)
        if not args.keep_existing:
            for image in dossier.iterdir():
                if image.suffix.lower() in {".png", ".jpg", ".jpeg"}:
                    image.unlink()
        compteurs[categorie], n_faibles = generer_categorie(
            pipe, categorie, args.n_par_categorie, args.output_dir,
            device, SEED + 10_000 * CATEGORIES.index(categorie),
        )
        faibles += n_faibles
        print(f"{categorie} : {compteurs[categorie]} images")

    ecrire_log(compteurs, args.output_dir, device, faibles, args.n_par_categorie)
    grille = sauvegarder_grille(args.output_dir, args.categories)
    print(f"LOG : {args.output_dir / LOG_PATH.name}")
    print(f"Grille : {grille}")


if __name__ == "__main__":
    main()

"""Compare les images copy-paste et diffusion.

L'ancien R3 archivé est identique à R1 : le copy-paste n'a donc jamais été
correctement évalué. Seules ses métriques de génération (FID, distance,
quasi-duplication) sont exploitables. Les colonnes de performance R3 restent
vides pour cette méthode et le statut est explicite dans le CSV.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

ANCIEN = Path("results/archive_copy_paste")
NOUVEAU = Path("results")
SORTIE = NOUVEAU / "comparaison_methodes.csv"
CATEGORIES = ("bottle", "cable", "transistor")
SEUILS = (0.05, 0.10)
MESSAGE_R3_INVALIDE = (
    "R3 archive identique a R1 (datamodule reconstruit) : "
    "performance non attribuable au copy-paste"
)


def agreger_resultats_r3(chemin: Path) -> pd.DataFrame:
    df = pd.read_csv(chemin)
    df = df[df["regime"] == "R3_synthetique"]
    df = df.drop_duplicates(subset=["categorie", "regime", "seed"], keep="last")
    agg = df.groupby("categorie")[["auroc_image", "auroc_pixel", "aupro"]].agg(["mean", "std"])
    agg.columns = [f"{metrique}_{stat}" for metrique, stat in agg.columns]
    return agg.reset_index()


def taux_sous_seuil(racine: Path, categorie: str, seuil: float) -> float:
    chemin = racine / f"distances_quasi_duplication_{categorie}.csv"
    if not chemin.exists():
        return float("nan")
    distances = pd.read_csv(chemin)["distance"].to_numpy()
    return float(np.mean(distances < seuil))


def construire_table(racine: Path, methode: str, r3_valide: bool) -> pd.DataFrame:
    generatives = pd.read_csv(racine / "generative_metrics.csv")
    if r3_valide:
        resultats = agreger_resultats_r3(racine / "results.csv")
        table = resultats.merge(
            generatives[["categorie", "n_synth", "fid", "distance_mediane_reel_vers_synth"]],
            on="categorie",
            how="left",
        )
    else:
        table = generatives[["categorie", "n_synth", "fid", "distance_mediane_reel_vers_synth"]].copy()
        for colonne in [
            "auroc_image_mean",
            "auroc_image_std",
            "auroc_pixel_mean",
            "auroc_pixel_std",
            "aupro_mean",
            "aupro_std",
        ]:
            table[colonne] = np.nan
    table["methode"] = methode
    table["n_synthetiques"] = table.pop("n_synth")
    table["distance_mediane"] = table.pop("distance_mediane_reel_vers_synth")
    for seuil in SEUILS:
        table[f"taux_quasi_duplication_{seuil:.2f}"] = [
            taux_sous_seuil(racine, categorie, seuil) for categorie in table["categorie"]
        ]
    table = table[
        [
            "methode",
            "categorie",
            "n_synthetiques",
            "auroc_image_mean",
            "auroc_image_std",
            "auroc_pixel_mean",
            "auroc_pixel_std",
            "aupro_mean",
            "aupro_std",
            "fid",
            "distance_mediane",
            "taux_quasi_duplication_0.05",
            "taux_quasi_duplication_0.10",
        ]
    ]
    return table


def ajouter_moyenne(table: pd.DataFrame) -> pd.DataFrame:
    lignes = []
    for methode, bloc in table.groupby("methode", sort=False):
        ligne = {"methode": methode, "categorie": "moyenne"}
        for colonne in table.columns:
            if colonne in {"methode", "categorie"}:
                continue
            if colonne == "n_synthetiques":
                ligne[colonne] = bloc[colonne].sum()
            else:
                ligne[colonne] = bloc[colonne].mean()
        lignes.append(ligne)
    return pd.concat([table, pd.DataFrame(lignes)], ignore_index=True)


def main() -> None:
    ancienne = construire_table(ANCIEN, "copy_paste_reference", r3_valide=False)
    nouvelle = construire_table(NOUVEAU, "diffusion_inpainting", r3_valide=True)
    table = ajouter_moyenne(pd.concat([ancienne, nouvelle], ignore_index=True))
    table = table.sort_values(
        ["methode", "categorie"],
        key=lambda serie: serie.map({"copy_paste_reference": 0, "diffusion_inpainting": 1})
        if serie.name == "methode"
        else serie.map({cat: i for i, cat in enumerate((*CATEGORIES, "moyenne"))}),
    )
    table["r3_valide"] = table["methode"].eq("diffusion_inpainting")
    table["commentaire"] = np.where(
        table["r3_valide"], "R3 recalcule avec les synthetiques injectes", MESSAGE_R3_INVALIDE
    )
    table.to_csv(SORTIE, index=False)
    print(table.to_string(index=False))
    print(f"\nComparaison sauvegardée : {SORTIE}")


if __name__ == "__main__":
    main()

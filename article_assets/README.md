# Images pour l'article

Ce dossier contient une sélection d'images synthétiques **utilisées comme échantillons
d'entraînement normaux (R3)** dans l'expérience de diffusion. Elles sont fournies en
256 × 256, directement utilisables dans un article ou une présentation.

## Planche complète

La planche de synthèse est déjà versionnée ici :

- `figures/fig_synthetiques_diffusion_exemples.png`

## Sélection individuelle

6 images par catégorie sont copiées dans `article_assets/synthetiques/<catégorie>/`.
Les indices couvrent les trois types de défaut conçus pour chaque catégorie.

| Catégorie | Fichiers | Types de défaut |
|:---|:---|:---|
| bottle | `synth_000.png`, `synth_003.png` | fissure |
| bottle | `synth_001.png`, `synth_004.png` | contamination |
| bottle | `synth_002.png`, `synth_005.png` | éclat |
| cable | `synth_000.png`, `synth_003.png` | coupure |
| cable | `synth_001.png`, `synth_004.png` | isolant arraché |
| cable | `synth_002.png`, `synth_005.png` | câble déformé |
| transistor | `synth_000.png`, `synth_003.png` | boîtier endommagé |
| transistor | `synth_001.png`, `synth_004.png` | broche tordue |
| transistor | `synth_002.png`, `synth_005.png` | broche coupée |

## Provenance

- Modèle : Stable Diffusion v1.5 Inpainting, sans fine-tuning.
- Conditionnement : images `train/good` de MVTec AD + masques procéduraux.
- **Aucune image ni masque du split test n'a été utilisé pour générer ces images.**
- Graine globale : `42`.
- Paramètres complets : `synthetiques/LOG_diffusion.txt`.

Les images complètes (120 par catégorie) restent dans `synthetiques/` et ne sont pas
versionnées en raison de leur volume. Les 18 fichiers de ce dossier sont un sous-ensemble
représentatif pour l'article.

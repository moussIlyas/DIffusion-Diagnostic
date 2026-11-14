# IND-3 : Défauts synthétiques par diffusion pour l'inspection visuelle

Ce dépôt compare trois régimes d'entraînement pour la détection d'anomalies MVTec AD
(`bottle`, `cable`, `transistor`) :

- **R1** : réel seul (`train/good`).
- **R2** : augmentation classique.
- **R3** : réel + défauts synthétiques.

Les défauts synthétiques sont générés avec **Stable Diffusion v1.5 Inpainting**, à partir
des seules images `train/good` et de masques procéduraux. **Le split test n'est jamais
utilisé pour entraîner ou guider le générateur.**

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Le premier lancement du générateur télécharge le modèle
`stable-diffusion-v1-5/stable-diffusion-inpainting` depuis Hugging Face. Pour le mettre en
cache localement :

```bash
export HF_HOME=./.cache/huggingface
```

Un GPU CUDA est fortement recommandé. Le générateur accepte aussi `--device cpu`, mais
sera beaucoup plus lent.

## Générer les défauts synthétiques

```bash
HF_HOME=./.cache/huggingface python generer_synthetiques_diffusion.py
```

Par défaut :

- 120 images par catégorie ;
- sortie dans `synthetiques/<catégorie>/synth_XXX.png` en 256 × 256 ;
- journal dans `synthetiques/LOG_diffusion.txt` ;
- planche d'exemples dans `figures/fig_synthetiques_diffusion_exemples.png`.

Options utiles :

```bash
python generer_synthetiques_diffusion.py \
  --n-par-categorie 120 \
  --categories bottle cable transistor \
  --output-dir synthetiques \
  --device cuda
```

## Évaluer les trois régimes

Le notebook d'évaluation est `notebook_IND3_diffusion_defauts.ipynb` :

```bash
jupyter nbconvert --to notebook --execute notebook_IND3_diffusion_defauts.ipynb \
  --ExecutePreprocessor.timeout=0 \
  --stdout > /dev/null
```

La cellule 5 (`executer_experiences()`) est idempotente : elle relit `results/results.csv`
et saute les combinaisons déjà présentes. Pour ne relancer que cette cellule, l'exécuter
depuis Jupyter.

### Point critique pour R3

Dans le notebook, les images synthétiques sont injectées dans le datamodule. Ensuite,
Lightning appelle `setup("fit")` et reconstruit ce datamodule : les images injectées sont
perdues et **R3 devient strictement identique à R1**.

Pour obtenir un vrai R3, il faut conserver le datamodule déjà préparé avec
`datamodule._is_setup = True` après l'injection, avant `trainer.fit`. L'évaluation de ce
dépôt a été faite dans une **copie temporaire** du notebook avec cette seule correction ;
`notebook_IND3_diffusion_defauts.ipynb` et `generer_synthetiques.ipynb` restent inchangés.

Les 9 runs R3 corrigés (3 catégories × 3 graines) sont disponibles dans
`results/results.csv` et `results/predictions_R3_synthetique_*.csv`.

## Comparer copy-paste et diffusion

```bash
python comparer_methodes.py
```

Le script produit `results/comparaison_methodes.csv` avec, par catégorie :

- FID ;
- distance médiane au plus proche défaut réel ;
- taux de quasi-duplication aux seuils 0,05 et 0,10 ;
- AUROC image, AUROC pixel et AUPRO **uniquement pour la diffusion**.

### Avertissement sur l'ancien copy-paste

L'ancien générateur `generer_synthetiques.ipynb` construit ses images à partir des défauts
et des masques de `data/<catégorie>/test` et `data/<catégorie>/ground_truth` : sa génération
utilise donc directement le split test.

De plus, son R3 archivé est **identique à R1 à toutes les graines** : le copy-paste n'a
jamais été correctement évalué. Ses colonnes AUROC/AUPRO sont donc laissées vides dans
`results/comparaison_methodes.csv` ; seuls son FID, sa distance et sa quasi-duplication
sont comparables. Les anciennes valeurs de performance R3 ne doivent pas être attribuées
au copy-paste.

La méthode diffusion est la seule des deux qui n'utilise jamais le test et dont le R3 a
été réellement recalculé.

## Structure des livrables

- `generer_synthetiques_diffusion.py` : générateur de défauts par inpainting.
- `comparer_methodes.py` : comparaison copy-paste / diffusion.
- `synthetiques/<catégorie>/` : 120 images synthétiques par catégorie.
- `synthetiques/LOG_diffusion.txt` : paramètres et graine de génération.
- `results/results.csv` : résultats bruts R1, R2 et R3 corrigé.
- `results/summary.csv` : moyenne ± écart-type par régime.
- `results/gain_relatif.csv` : comparaison R2 → R3.
- `results/generative_metrics.csv` : FID, couverture et quasi-duplication.
- `results/comparaison_methodes.csv` : comparaison des générateurs (R3 valide pour la diffusion uniquement).
- `results/validation_quasi_duplication_reelle.csv` : contrôle du seuil sur les vrais défauts.
- `results/validation_diffusion_locale.csv` : contrôle local des zones générées.
- `results/ablations_aug.csv` : ablations data-aug.
- `results/ablations_synth.csv` : ablation du filtrage synthétique.
- `results/distances_quasi_duplication_*.csv` : distances au plus proche vrai défaut.
- `results/README_results.md` : rapport complet, limites et interprétation.
- `figures/*.png` : figures au format PNG 150 dpi.
- `article_assets/` : sélection d'images synthétiques et légendes pour l'article.

## Images pour l'article

- Planche complète : `figures/fig_synthetiques_diffusion_exemples.png`.
- Sélection de 6 images par catégorie : `article_assets/synthetiques/<catégorie>/`.
- Correspondance entre fichiers et types de défaut : `article_assets/README.md`.

Ces images sont des exemples synthétiques **ajoutés au train du régime R3**. Elles ne
proviennent pas du split test.

## Résultats principaux

| Catégorie | R3 AUROC pixel | R3 AUPRO | FID |
|---|---:|---:|---:|
| bottle | 0,9847 | 0,9423 | 69,00 |
| cable | 0,9818 | 0,9268 | 68,05 |
| transistor | 0,9723 | 0,9456 | 95,03 |

R3 corrigé est légèrement inférieur à R1 sur AUROC pixel et AUPRO, mais reste nettement
supérieur à R2. Le FID est sous 100 pour les trois catégories. Le taux de
quasi-duplication reste élevé ; ce seuil ne sépare pas correctement les défauts réels entre
eux et doit être lu avec la distance médiane et le FID. Le détail est dans
`results/README_results.md`.

## Note importante

Les images de défauts réels utilisées dans l'analyse de quasi-duplication et le FID
proviennent **uniquement du split test** de MVTec AD. Elles servent de galerie de référence
et ne sont jamais utilisées pour l'entraînement ni la sélection de modèle du pipeline
diffusion.

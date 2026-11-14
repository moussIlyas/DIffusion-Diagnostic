# IND-3 : Défauts synthétiques par diffusion pour l'inspection visuelle

## Installation

```bash
pip install -r requirements.txt
```

## Lancement du notebook

Ouvrir `notebook_IND3_diffusion_defauts.ipynb` dans Jupyter et exécuter les cellules dans l'ordre.

## Relancer uniquement la cellule d'entraînement

La cellule 5 (`executer_experiences()`) est idempotente : elle relit `results.csv` et saute les combinaisons déjà effectuées.

```python
# Dans une cellule du notebook :
executer_experiences()
```

Ou en ligne de commande avec `jupyter nbconvert` :

```bash
jupyter nbconvert --to notebook --execute notebook_IND3_diffusion_defauts.ipynb \
  --ExecutePreprocessor.timeout=0 \
  --stdout > /dev/null
```

Pour n'exécuter que la cellule 5, il suffit de relancer cette cellule seule depuis Jupyter.

## Structure des livrables

- `results/results.csv` : résultats bruts de toutes les runs
- `results/summary.csv` : moyenne ± écart-type par régime
- `results/ablations_aug.csv` : ablations data-aug
- `results/ablations_synth.csv` : ablation filtrage synthétique
- `results/distances_quasi_duplication_*.csv` : distances au plus proche vrai défaut
- `figures/*.png` : figures au format PNG 150 dpi
- `results/README_results.md` : rapport automatique

## Note importante

Les images de défauts réels utilisées dans l'analyse de quasi-duplication proviennent **uniquement du split test** de MVTec AD. Elles servent de galerie de référence pour le calcul de distance (comme le FID) et ne sont jamais utilisées pour l'entraînement ni la sélection de modèle.

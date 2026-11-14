# Rapport de résultats — IND-3

## Résumé des métriques par régime

| categorie   | regime           | auroc_image        | auroc_image.1   | auroc_pixel        | auroc_pixel.1   | aupro              | aupro.1   |
|:------------|:-----------------|:-------------------|:----------------|:-------------------|:----------------|:-------------------|:----------|
| nan         | nan              | mean               | std             | mean               | std             | mean               | std       |
| bottle      | R1_reel_seul     | 1.0                | nan             | 0.9856631755828856 | nan             | 0.9452453851699828 | nan       |
| bottle      | R2_aug_classique | 0.9920635223388672 | nan             | 0.975239396095276  | nan             | 0.9030372500419616 | nan       |
| cable       | R1_reel_seul     | 0.9906296730041504 | nan             | 0.9847263097763062 | nan             | 0.9303470849990844 | nan       |
| cable       | R2_aug_classique | 0.9765742421150208 | nan             | 0.97274649143219   | nan             | 0.9130930304527284 | nan       |
| transistor  | R1_reel_seul     | 0.9925000071525574 | nan             | 0.9727544784545898 | nan             | 0.9461668729782104 | nan       |
| transistor  | R2_aug_classique | 0.9470833539962769 | nan             | 0.9210352897644044 | nan             | 0.89891517162323   | nan       |



## Résultats bruts

| categorie   | regime           |   seed |   auroc_image |   auroc_pixel |    aupro | timestamp                  |
|:------------|:-----------------|-------:|--------------:|--------------:|---------:|:---------------------------|
| bottle      | R1_reel_seul     |     42 |      1        |      0.985663 | 0.945245 | 2026-11-14T12:35:20.069912 |
| bottle      | R2_aug_classique |     42 |      0.992064 |      0.975239 | 0.903037 | 2026-11-14T12:37:23.865135 |
| cable       | R1_reel_seul     |     42 |      0.99063  |      0.984726 | 0.930347 | 2026-11-14T12:39:02.393543 |
| cable       | R2_aug_classique |     42 |      0.976574 |      0.972746 | 0.913093 | 2026-11-14T12:41:01.995655 |
| transistor  | R1_reel_seul     |     42 |      0.9925   |      0.972754 | 0.946167 | 2026-11-14T12:42:39.526774 |
| transistor  | R2_aug_classique |     42 |      0.947083 |      0.921035 | 0.898915 | 2026-11-14T12:44:16.491406 |



## Ablations data-aug (R2)

| categorie   |   seed | ablation       |   auroc_image |   auroc_pixel |    aupro |
|:------------|-------:|:---------------|--------------:|--------------:|---------:|
| bottle      |     42 | flip_seul      |      1        |      0.985487 | 0.945106 |
| bottle      |     42 | rotation_seule |      1        |      0.985274 | 0.944081 |
| bottle      |     42 | bruit_seul     |      0.999206 |      0.980008 | 0.919089 |



## Note méthodologique

> Les images de défauts réels utilisées dans l'analyse de quasi-duplication proviennent **uniquement du split test** de MVTec AD. 

> Elles servent de **galerie de référence** pour le calcul de distance (comme le FID) et ne sont **jamais utilisées** pour l'entraînement ni la sélection de modèle. 



## Figures générées

- fig10_ablations.png
- fig1_auroc_par_regime.png
- fig2_aupro_par_regime.png
- fig3_heatmap_auroc.png
- fig4_auroc_par_graine_R1_reel_seul.png
- fig4_auroc_par_graine_R2_aug_classique.png
- fig4_auroc_par_graine_R3_synthetique.png
- fig5_exemples_bottle.png
- fig5_exemples_cable.png
- fig5_exemples_transistor.png
- fig6_analyse_erreurs.png
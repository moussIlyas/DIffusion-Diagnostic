# Rapport de résultats — IND-3

## Résumé des métriques par régime

| categorie   | regime           | auroc_image        | auroc_image.1         | auroc_pixel        | auroc_pixel.1          | aupro              | aupro.1                |
|:------------|:-----------------|:-------------------|:----------------------|:-------------------|:-----------------------|:-------------------|:-----------------------|
| nan         | nan              | mean               | std                   | mean               | std                    | mean               | std                    |
| bottle      | R1_reel_seul     | 1.0                | 0.0                   | 0.9855995923280716 | 4.429106076002488e-05  | 0.9449001848697662 | 0.00031005744399523584 |
| bottle      | R2_aug_classique | 0.9946428835391998 | 0.001875315666619464  | 0.9772861599922181 | 0.0018163704348758325  | 0.9094821810722351 | 0.0067637977869373644  |
| bottle      | R3_synthetique   | 1.0                | 0.0                   | 0.9855995923280716 | 4.429106076002488e-05  | 0.9449001848697662 | 0.00031005744399523584 |
| cable       | R1_reel_seul     | 0.98777174949646   | 0.0037834620012891    | 0.9849213361740112 | 0.00023296931698852836 | 0.931259512901306  | 0.0009739953633340605  |
| cable       | R2_aug_classique | 0.9755903333425523 | 0.0010307584748154724 | 0.9723271876573563 | 0.0007777931063294682  | 0.9144940972328186 | 0.0020787160168657982  |
| cable       | R3_synthetique   | 0.98777174949646   | 0.0037834620012891    | 0.9849213361740112 | 0.00023296931698852836 | 0.931259512901306  | 0.0009739953633340605  |
| transistor  | R1_reel_seul     | 0.9944791197776794 | 0.0013766398180033415 | 0.9734121561050415 | 0.0006465449484132475  | 0.9471641927957535 | 0.0009115251382969963  |
| transistor  | R2_aug_classique | 0.9419166803359985 | 0.0034434864436850695 | 0.9207632064819335 | 0.004356179391019311   | 0.8956506729125977 | 0.003990497972999785   |
| transistor  | R3_synthetique   | 0.9944999575614929 | 0.0011931152323038639 | 0.9733216047286988 | 0.000595409973486224   | 0.9470543146133423 | 0.0008267554857153813  |



## Résultats bruts

| categorie   | regime           |   seed |   auroc_image |   auroc_pixel |    aupro | timestamp                  |
|:------------|:-----------------|-------:|--------------:|--------------:|---------:|:---------------------------|
| bottle      | R1_reel_seul     |     42 |      1        |      0.985663 | 0.945245 | 2026-11-14T12:35:20.069912 |
| bottle      | R2_aug_classique |     42 |      0.992064 |      0.975239 | 0.903037 | 2026-11-14T12:37:23.865135 |
| cable       | R1_reel_seul     |     42 |      0.99063  |      0.984726 | 0.930347 | 2026-11-14T12:39:02.393543 |
| cable       | R2_aug_classique |     42 |      0.976574 |      0.972746 | 0.913093 | 2026-11-14T12:41:01.995655 |
| transistor  | R1_reel_seul     |     42 |      0.9925   |      0.972754 | 0.946167 | 2026-11-14T12:42:39.526774 |
| transistor  | R2_aug_classique |     42 |      0.947083 |      0.921035 | 0.898915 | 2026-11-14T12:44:16.491406 |
| bottle      | R3_synthetique   |     42 |      1        |      0.985663 | 0.945245 | 2026-11-14T14:00:39.591203 |
| cable       | R3_synthetique   |     42 |      0.99063  |      0.984726 | 0.930347 | 2026-11-14T14:04:54.576561 |
| transistor  | R3_synthetique   |     42 |      0.9925   |      0.972754 | 0.946167 | 2026-11-14T14:06:33.221712 |
| bottle      | R1_reel_seul     |     43 |      1        |      0.98556  | 0.944491 | 2026-11-14T14:07:49.657734 |
| bottle      | R2_aug_classique |     43 |      0.994444 |      0.976273 | 0.904243 | 2026-11-14T14:09:03.963756 |
| bottle      | R3_synthetique   |     43 |      1        |      0.98556  | 0.944491 | 2026-11-14T14:10:12.937776 |
| cable       | R1_reel_seul     |     43 |      0.982196 |      0.984713 | 0.930488 | 2026-11-14T14:11:50.620082 |
| cable       | R2_aug_classique |     43 |      0.974138 |      0.971161 | 0.912335 | 2026-11-14T14:13:50.875571 |
| cable       | R3_synthetique   |     43 |      0.982196 |      0.984713 | 0.930488 | 2026-11-14T14:15:43.385396 |
| transistor  | R1_reel_seul     |     43 |      0.994583 |      0.972959 | 0.946615 | 2026-11-14T14:17:23.260539 |
| transistor  | R2_aug_classique |     43 |      0.9425   |      0.925049 | 0.898383 | 2026-11-14T14:19:26.553358 |
| transistor  | R2_aug_classique |     43 |      0.9425   |      0.925049 | 0.898383 | 2026-11-14T14:19:42.307484 |
| transistor  | R3_synthetique   |     43 |      0.994583 |      0.972959 | 0.946615 | 2026-11-14T14:21:23.630572 |
| transistor  | R3_synthetique   |     43 |      0.994583 |      0.972959 | 0.946615 | 2026-11-14T14:21:40.107448 |
| bottle      | R1_reel_seul     |     44 |      1        |      0.985587 | 0.944932 | 2026-11-14T14:23:04.778651 |
| bottle      | R1_reel_seul     |     44 |      1        |      0.985587 | 0.944932 | 2026-11-14T14:23:21.087717 |
| bottle      | R2_aug_classique |     44 |      0.996032 |      0.978816 | 0.915324 | 2026-11-14T14:24:43.067490 |
| bottle      | R2_aug_classique |     44 |      0.996032 |      0.978816 | 0.915324 | 2026-11-14T14:25:01.276954 |
| bottle      | R3_synthetique   |     44 |      1        |      0.985587 | 0.944932 | 2026-11-14T14:26:16.409558 |
| bottle      | R3_synthetique   |     44 |      1        |      0.985587 | 0.944932 | 2026-11-14T14:26:35.307248 |
| cable       | R1_reel_seul     |     44 |      0.98913  |      0.985123 | 0.932102 | 2026-11-14T14:28:26.307749 |
| cable       | R1_reel_seul     |     44 |      0.98913  |      0.985123 | 0.932102 | 2026-11-14T14:28:44.328154 |
| cable       | R2_aug_classique |     44 |      0.975825 |      0.972701 | 0.916274 | 2026-11-14T14:30:56.343908 |
| cable       | R2_aug_classique |     44 |      0.975825 |      0.972701 | 0.916274 | 2026-11-14T14:31:15.430263 |
| cable       | R3_synthetique   |     44 |      0.98913  |      0.985123 | 0.932102 | 2026-11-14T14:33:18.492592 |
| cable       | R3_synthetique   |     44 |      0.98913  |      0.985123 | 0.932102 | 2026-11-14T14:33:37.463147 |
| transistor  | R1_reel_seul     |     44 |      0.995417 |      0.973967 | 0.947938 | 2026-11-14T14:35:20.244289 |
| transistor  | R1_reel_seul     |     44 |      0.995417 |      0.973967 | 0.947938 | 2026-11-14T14:35:39.378755 |
| transistor  | R2_aug_classique |     44 |      0.93875  |      0.916342 | 0.891286 | 2026-11-14T14:37:20.779810 |
| transistor  | R2_aug_classique |     44 |      0.93875  |      0.916342 | 0.891286 | 2026-11-14T14:37:39.618178 |
| transistor  | R3_synthetique   |     44 |      0.995417 |      0.973967 | 0.947938 | 2026-11-14T14:39:16.226101 |
| transistor  | R3_synthetique   |     44 |      0.995417 |      0.973967 | 0.947938 | 2026-11-14T14:39:35.155278 |



## Ablations data-aug (R2)

| categorie   |   seed | ablation       |   auroc_image |   auroc_pixel |    aupro |
|:------------|-------:|:---------------|--------------:|--------------:|---------:|
| bottle      |     42 | flip_seul      |      1        |      0.985487 | 0.945106 |
| bottle      |     42 | rotation_seule |      1        |      0.985274 | 0.944081 |
| bottle      |     42 | bruit_seul     |      0.999206 |      0.980008 | 0.919089 |



## Ablations synthétiques (R3 filtré)

| categorie   |   seed | ablation      |     seuil |   auroc_image |   auroc_pixel |    aupro |
|:------------|-------:|:--------------|----------:|--------------:|--------------:|---------:|
| bottle      |     42 | synth_filtree | 0.0192721 |             1 |      0.985663 | 0.945245 |



## Note méthodologique

> Les images de défauts réels utilisées dans l'analyse de quasi-duplication proviennent **uniquement du split test** de MVTec AD. 

> Elles servent de **galerie de référence** pour le calcul de distance (comme le FID) et ne sont **jamais utilisées** pour l'entraînement ni la sélection de modèle. 



## Figures générées

- fig10_ablations.png
- fig11_gain_relatif.png
- fig12_auroc_classes_rares.png
- fig13_fid_couverture.png
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
- fig7_histogramme_distances_bottle.png
- fig7_histogramme_distances_cable.png
- fig7_histogramme_distances_transistor.png
- fig8_taux_quasi_duplication_bottle.png
- fig8_taux_quasi_duplication_cable.png
- fig8_taux_quasi_duplication_transistor.png
- fig9_exemples_voisins_bottle.png
- fig9_exemples_voisins_cable.png
- fig9_exemples_voisins_transistor.png
- fig_synthetiques_exemples_bottle.png
- fig_synthetiques_exemples_cable.png
- fig_synthetiques_exemples_transistor.png
# Rapport de résultats — IND-3

## Résumé des métriques par régime

| Catégorie | Régime | AUROC image | AUROC pixel | AUPRO |
|:---|:---|---:|---:|---:|
| bottle | R1 — réel seul | 1,0000 ± 0,0000 | 0,9856 ± 0,0001 | 0,9449 ± 0,0004 |
| bottle | R2 — aug. classique | 0,9942 ± 0,0020 | 0,9768 ± 0,0018 | 0,9075 ± 0,0068 |
| bottle | R3 — synthétique | 1,0000 ± 0,0000 | 0,9847 ± 0,0000 | 0,9423 ± 0,0003 |
| cable | R1 — réel seul | 0,9873 ± 0,0045 | 0,9849 ± 0,0002 | 0,9310 ± 0,0010 |
| cable | R2 — aug. classique | 0,9755 ± 0,0012 | 0,9722 ± 0,0009 | 0,9139 ± 0,0021 |
| cable | R3 — synthétique | 0,9815 ± 0,0022 | 0,9818 ± 0,0002 | 0,9268 ± 0,0006 |
| transistor | R1 — réel seul | 0,9942 ± 0,0015 | 0,9732 ± 0,0006 | 0,9469 ± 0,0009 |
| transistor | R2 — aug. classique | 0,9428 ± 0,0042 | 0,9208 ± 0,0044 | 0,8962 ± 0,0043 |
| transistor | R3 — synthétique | 0,9921 ± 0,0011 | 0,9723 ± 0,0005 | 0,9456 ± 0,0009 |

## Résultats bruts

| categorie   | regime           |   seed |   auroc_image |   auroc_pixel |    aupro | timestamp                  |
|:------------|:-----------------|-------:|--------------:|--------------:|---------:|:---------------------------|
| bottle      | R1_reel_seul     |     42 |      1        |      0.985663 | 0.945245 | 2026-11-14T12:35:20.069912 |
| bottle      | R2_aug_classique |     42 |      0.992064 |      0.975239 | 0.903037 | 2026-11-14T12:37:23.865135 |
| cable       | R1_reel_seul     |     42 |      0.99063  |      0.984726 | 0.930347 | 2026-11-14T12:39:02.393543 |
| cable       | R2_aug_classique |     42 |      0.976574 |      0.972746 | 0.913093 | 2026-11-14T12:41:01.995655 |
| transistor  | R1_reel_seul     |     42 |      0.9925   |      0.972754 | 0.946167 | 2026-11-14T12:42:39.526774 |
| transistor  | R2_aug_classique |     42 |      0.947083 |      0.921035 | 0.898915 | 2026-11-14T12:44:16.491406 |
| bottle      | R1_reel_seul     |     43 |      1        |      0.98556  | 0.944491 | 2026-11-14T14:07:49.657734 |
| bottle      | R2_aug_classique |     43 |      0.994444 |      0.976273 | 0.904243 | 2026-11-14T14:09:03.963756 |
| cable       | R1_reel_seul     |     43 |      0.982196 |      0.984713 | 0.930488 | 2026-11-14T14:11:50.620082 |
| cable       | R2_aug_classique |     43 |      0.974138 |      0.971161 | 0.912335 | 2026-11-14T14:13:50.875571 |
| transistor  | R1_reel_seul     |     43 |      0.994583 |      0.972959 | 0.946615 | 2026-11-14T14:17:23.260539 |
| transistor  | R2_aug_classique |     43 |      0.9425   |      0.925049 | 0.898383 | 2026-11-14T14:19:42.307484 |
| bottle      | R1_reel_seul     |     44 |      1        |      0.985587 | 0.944932 | 2026-11-14T14:23:21.087717 |
| bottle      | R2_aug_classique |     44 |      0.996032 |      0.978816 | 0.915324 | 2026-11-14T14:25:01.276954 |
| cable       | R1_reel_seul     |     44 |      0.98913  |      0.985123 | 0.932102 | 2026-11-14T14:28:44.328154 |
| cable       | R2_aug_classique |     44 |      0.975825 |      0.972701 | 0.916274 | 2026-11-14T14:31:15.430263 |
| transistor  | R1_reel_seul     |     44 |      0.995417 |      0.973967 | 0.947938 | 2026-11-14T14:35:39.378755 |
| transistor  | R2_aug_classique |     44 |      0.93875  |      0.916342 | 0.891286 | 2026-11-14T14:37:39.618178 |
| bottle      | R3_synthetique   |     42 |      1        |      0.984726 | 0.942438 | 2026-11-14T16:15:44.722178 |
| cable       | R3_synthetique   |     42 |      0.97901  |      0.981525 | 0.926538 | 2026-11-14T16:18:33.297702 |
| transistor  | R3_synthetique   |     42 |      0.9925   |      0.971743 | 0.944607 | 2026-11-14T16:21:19.745616 |
| bottle      | R3_synthetique   |     43 |      1        |      0.984686 | 0.941999 | 2026-11-14T16:23:34.416565 |
| cable       | R3_synthetique   |     43 |      0.982759 |      0.981853 | 0.926457 | 2026-11-14T16:26:14.639223 |
| transistor  | R3_synthetique   |     43 |      0.992917 |      0.972591 | 0.94579  | 2026-11-14T16:28:52.367703 |
| bottle      | R3_synthetique   |     44 |      1        |      0.98465  | 0.942546 | 2026-11-14T16:31:05.646457 |
| cable       | R3_synthetique   |     44 |      0.982759 |      0.981873 | 0.927544 | 2026-11-14T16:33:45.993543 |
| transistor  | R3_synthetique   |     44 |      0.990833 |      0.972609 | 0.946285 | 2026-11-14T16:36:23.871627 |



## Ablations data-aug (R2)

| categorie   |   seed | ablation       |   auroc_image |   auroc_pixel |    aupro |
|:------------|-------:|:---------------|--------------:|--------------:|---------:|
| bottle      |     42 | flip_seul      |      1        |      0.985487 | 0.945106 |
| bottle      |     42 | rotation_seule |      1        |      0.985274 | 0.944081 |
| bottle      |     42 | bruit_seul     |      0.999206 |      0.980008 | 0.919089 |



## Ablations synthétiques (R3 filtré)

| categorie   |   seed | ablation      |     seuil |   auroc_image |   auroc_pixel |    aupro |
|:------------|-------:|:--------------|----------:|--------------:|--------------:|---------:|
| bottle      |     42 | synth_filtree | 0.0184995 |             1 |      0.984672 | 0.943407 |



## Note méthodologique

> Les images de défauts réels utilisées dans l'analyse de quasi-duplication proviennent **uniquement du split test** de MVTec AD.

> Elles servent de **galerie de référence** pour le calcul de distance (comme le FID) et ne sont **jamais utilisées** pour l'entraînement ni la sélection de modèle du pipeline diffusion.

> Exception historique : l'ancien générateur copy-paste (`generer_synthetiques.ipynb`) utilisait directement des défauts et masques test. Ses résultats sont donc biaisés, et son R3 archivé est identique à R1 : il n'a jamais été correctement évalué (voir la section diffusion ci-dessous).



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
- fig_synthetiques_diffusion_exemples.png
- fig_synthetiques_exemples_bottle.png
- fig_synthetiques_exemples_cable.png
- fig_synthetiques_exemples_transistor.png

> Les figures `fig_synthetiques_exemples_*` correspondent à l'ancien copy-paste (référence biaisée).
> La figure `fig_synthetiques_diffusion_exemples.png` correspond à la nouvelle méthode sans fuite du test.
<!-- DEBUT_SECTION_DIFFUSION -->
## Mise à jour — défauts synthétiques par diffusion

### Générateur utilisé

- Modèle : **Stable Diffusion v1.5 Inpainting** préentraîné, sans fine-tuning.
- Conditionnement : uniquement des images **`train/good`** de MVTec AD.
- Masques de défaut : **procéduraux**, dessinés localement (fissures, taches, éclats,
  coupures, érosion, déformations).
- Aucune image, aucun masque et aucune métadonnée du split **test** ne sont utilisés
  pour entraîner ou guider le générateur.
- 120 images par catégorie, sauvegardées en 256 × 256 dans `synthetiques/<catégorie>/`.
- Graine fixe : `42`; journal complet : `synthetiques/LOG_diffusion.txt`.
- Planche d'exemples : `figures/fig_synthetiques_diffusion_exemples.png`.

### Correction nécessaire de l'exécution R3

Sans correction, les images synthétiques sont ajoutées au dataset, puis Lightning appelle
`setup("fit")` et reconstruit le datamodule : les 120 images sont silencieusement perdues.
R3 était donc strictement identique à R1.

Pour cette évaluation, la seule correction appliquée est `datamodule._is_setup = True`
après l'injection, dans une **copie temporaire** du notebook. Les deux notebooks originaux
n'ont pas été modifiés. Ce point est indispensable pour interpréter R3.

R3 corrigé n'est plus identique à R1, mais reste légèrement inférieur :

- **bottle** : Δ AUROC pixel = -0.00092, Δ AUPRO = -0.00256.
- **cable** : Δ AUROC pixel = -0.00310, Δ AUPRO = -0.00413.
- **transistor** : Δ AUROC pixel = -0.00091, Δ AUPRO = -0.00135.

R3 conserve en revanche un gain net sur R2 (augmentation classique), avec des gains AUPRO de **+1,42 % à +5,51 %** selon la catégorie.

### Comparaison des générateurs

| Méthode                | Catégorie   |   Images | AUROC image   | ± std image   | AUROC pixel   | ± std pixel   | AUPRO   | ± std AUPRO   |    FID |   Distance médiane | Dup. < 0,05   | Dup. < 0,10   |
|:-----------------------|:------------|---------:|:--------------|:--------------|:--------------|:--------------|:--------|:--------------|-------:|-------------------:|:--------------|:--------------|
| Copy-paste (référence) | bottle      |      120 | —             | —             | —             | —             | —       | —             | 41,099 |              0,016 | 97,5 %        | 100,0 %       |
| Copy-paste (référence) | cable       |      120 | —             | —             | —             | —             | —       | —             | 64,304 |              0,042 | 73,3 %        | 99,2 %        |
| Copy-paste (référence) | transistor  |      120 | —             | —             | —             | —             | —       | —             | 71,195 |              0,030 | 88,3 %        | 100,0 %       |
| Copy-paste (référence) | **moyenne** |      360 | —             | —             | —             | —             | —       | —             | 58,866 |              0,029 | 86,4 %        | 99,7 %        |
| Diffusion inpainting   | bottle      |      120 | 1,0000        | 0,0000        | 0,9847        | 0,0000        | 0,9423  | 0,0003        | 69,000 |              0,025 | 100,0 %       | 100,0 %       |
| Diffusion inpainting   | cable       |      120 | 0,9815        | 0,0022        | 0,9818        | 0,0002        | 0,9268  | 0,0006        | 68,054 |              0,044 | 90,8 %        | 100,0 %       |
| Diffusion inpainting   | transistor  |      120 | 0,9921        | 0,0011        | 0,9723        | 0,0005        | 0,9456  | 0,0009        | 95,035 |              0,032 | 96,7 %        | 100,0 %       |
| Diffusion inpainting   | **moyenne** |      360 | 0,9912        | 0,0011        | 0,9796        | 0,0002        | 0,9382  | 0,0006        | 77,363 |              0,034 | 95,8 %        | 100,0 %       |

**Point critique :** l'ancien R3 archivé est identique à R1 à toutes les graines. Le
copy-paste n'a donc **pas de score R3 exploitable** : ses colonnes AUROC/AUPRO sont laissées
vides. Seuls son FID, sa distance médiane et sa quasi-duplication sont comparables. Les
chiffres de performance R3 de l'ancienne archive ne doivent pas être présentés comme ceux
du copy-paste.

L'ancien copy-paste a un FID plus bas et une quasi-duplication plus faible, mais il construit
ses images à partir des défauts et masques de `data/<catégorie>/test` et
`data/<catégorie>/ground_truth`. Cette référence est donc biaisée par le test, et son R3
n'a jamais été correctement mesuré.

### Contrôle local des zones générées

Les masques ayant servi à la génération ont été reconstruits pour mesurer l'écart réel entre l'image `train/good` et l'image synthétique, uniquement dans la zone inpaintée. Les défauts occupent une petite surface (0.67 % à 1.62 % de l'image), avec un écart moyen local de 4.38 à 17.33 niveaux de gris et 2.9 % à 29.1 % de pixels modifiés de plus de 15 niveaux. Les images ne sont donc ni des copies de `train/good`, ni des copier-coller de défauts test. La plausibilité visuelle est à contrôler sur la planche `figures/fig_synthetiques_diffusion_exemples.png`.

Un contrôle CLIP sur l'image entière a aussi été essayé, mais il est peu sensible aux défauts industriels fins ; il n'est pas utilisé comme preuve de plausibilité dans ce rapport. Le CSV brut est conservé dans `results/validation_diffusion_clip_non_concluant.csv`.

### Contrôle de la métrique de quasi-duplication

La même distance cosinus a été calculée entre les vrais défauts du split test eux-mêmes. Ce contrôle montre que le seuil de 0,10 ne sépare pas des catégories différentes : il mesure surtout la ressemblance normale entre objets d'une même classe.

| Catégorie   |   Défauts réels |   Distance médiane réel-réel | Sous 0,05   | Sous 0,10   | Sous 0,15   |
|:------------|----------------:|-----------------------------:|:------------|:------------|:------------|
| bottle      |              63 |                        0,015 | 93,7 %      | 100,0 %     | 100,0 %     |
| cable       |              92 |                        0,039 | 88,0 %      | 100,0 %     | 100,0 %     |
| transistor  |              40 |                        0,022 | 87,5 %      | 100,0 %     | 100,0 %     |

### Bilan par rapport aux objectifs

- **R3 différent de R1** : oui, l'écart est faible mais réel sur les trois catégories.
- **FID < 100** : oui, avec 69,00 (`bottle`), 68,05 (`cable`) et 95,03 (`transistor`),
  soit 77,36 en moyenne.
- **Quasi-duplication < 90 %** : non. À 0,10, toutes les images sont comptées comme
  quasi-dupliquées ; à 0,05, le taux reste de 100 % (`bottle`), 90,8 % (`cable`) et
  96,7 % (`transistor`). L'objectif de 60–80 % n'est pas atteint.
- **Limite de la métrique** : les vrais défauts test sont eux-mêmes 100 % sous 0,10 et
  87,5–93,7 % sous 0,05 entre eux. Le seuil basé sur un plus proche voisin ne mesure donc
  pas correctement la duplication pour ce jeu de données.
- **Images plausibles** : les zones générées sont bien modifiées localement et ne sont pas
  des copier-coller, mais les défauts restent fins. Une validation visuelle humaine sur la
  planche d'exemples reste nécessaire.
- **Comparaison copy-paste** : impossible sur AUROC/AUPRO, car le R3 archivé est invalide.
  Les métriques de génération du copy-paste restent meilleures, mais elles sont obtenues
  avec une fuite du split test.

### Conclusion

La diffusion produit 360 images synthétiques sans utiliser le split test et recalcule un R3
réellement différent de R1. Elle reste meilleure que l'augmentation classique R2, mais
légèrement en retrait par rapport à R1 sur AUROC pixel et AUPRO. Le FID est sous 100 pour
les trois catégories. Le critère de quasi-duplication n'est pas satisfait. L'ancien
copy-paste affiche de meilleures métriques de génération, mais son R3 n'a jamais été
correctement évalué et sa génération utilise directement les défauts test : il ne constitue
pas une référence honnête.

Fichiers associés :

- `results/comparaison_methodes.csv`
- `results/generative_metrics.csv`
- `results/validation_quasi_duplication_reelle.csv`
- `results/validation_diffusion_locale.csv`
- `results/predictions_R3_synthetique_*.csv`
- `synthetiques/LOG_diffusion.txt`
- `figures/fig_synthetiques_diffusion_exemples.png`

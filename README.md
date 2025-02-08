# bataille_navale

Jeu de bataille navale contre l'ordi. Les startegies presentent plusieurs niveaux de 1 à 3, du tir aléatoire a une strategie assez simple (tir en damier en eliminant les zones impossibles : bateaux coulés et cases adjacences).
Niveau 3+, mi-statistiques mi machin learning avec un placement intelligent du damier, on obtient 80% contre un niveau 2 (evite bateau coule et les zones adjacences puis tire au hasard).
Quelques graphiques de comparaison 

La version  interessante est projetendgame.py qui en plus du niveau 3 y ajoute une interface graphique (exemple dans les fichiers de type graphisme____.png) + enregistrement en base de données (en locale donc requete sql pas préparée) en donnant un score a chaque compo humaine jouée contre lui. Il l'utilise pour affiner ses choix lors de statistiques egales dans la strategie 3+ plutot que de l'aleatoire. Il l'utilise aussi pour trouver de meilleurs strategies de placements des bateaux coté machine, selon le score que font contre lui les compos rentrés.

un extrait de la base de donnés dans bataille_navale.sql

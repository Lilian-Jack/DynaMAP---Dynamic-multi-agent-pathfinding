# DynaMAP---Dynamic-multi-agent-pathfinding
## Présentation
Le projet a pour objectif d'implémenter des algorithmes de pathfinding pour des agents placés sur un quadrillage. Les agents et leurs destinations sont placés au hasard sur une grille parsemé d'obstacles.  Les algorithmes (exemple : A*) doivent calculer le chemin optimal pour chaque agent jusqu'à sa destination. De plus, nôtre objectif est de supprimer les conflits entre agents : 
1. Les vertex conflicts : aucun agents ne doit se trouver au même moment sur la même position
2. Les edges conflicts : les agents ne doivent pas se croiser sur un même arc lorsqu'il échange de position

## Structure de données
*Classes
  * Robot : Implémente les  agents avec leurs positions actuelles, leurs spawns, leurs destination et le chemin suggéré par l'algorithme de pathfinding
  * Grille : Implémente le quadrillage sur lequel se trouvent les robots. Contient les robots et des fonctions qui permettent de connaître l'état de la grille. Par exemple, la fonction voisins permet aux robots de connaître les voisins possibles pour leurs prochain déplacement
  * Instance : Permet d'instancier une grille avec des agents, de l'afficher, de l'animer et de dérouler les différents algorithmes

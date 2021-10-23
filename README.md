# Jeu de la vie

Le jeu de la vie de Conway en Python

Version graphique utilisant PyGame

## Qu'est-ce que c'est ?

Le jeu de la vie est un automate cellulaire imaginé par John Horton Conway en 1970, je vous propose d'aller chercher sur Wikipédia pour lire la suite.

## Règles

Le jeu de la vie est un « jeu à zéro joueur », puisqu'il ne nécessite pas l'intervention du joueur lors de son déroulement. Il s’agit d’un automate cellulaire, un modèle où chaque état conduit mécaniquement à l’état suivant à partir de règles pré-établies.

Le jeu se déroule sur une grille à deux dimensions, théoriquement infinie (mais de longueur et de largeur finies et plus ou moins grandes dans la pratique), dont les cases — qu’on appelle des « cellules », par analogie avec les cellules vivantes — peuvent prendre deux états distincts : « vivante » ou « morte ».

Une cellule possède huit voisins, qui sont les cellules adjacentes horizontalement, verticalement et diagonalement.

À chaque étape, l’évolution d’une cellule est entièrement déterminée par l’état de ses huit voisines de la façon suivante :

    * une cellule morte possédant exactement trois voisines vivantes devient vivante (elle naît) ;
    * une cellule vivante possédant deux ou trois voisines vivantes le reste, sinon elle meurt.
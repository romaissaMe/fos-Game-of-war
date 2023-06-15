# fos-Game-of-war
Voici le nombre de chaque carte dans un jeu de cartes standard à 52 cartes, en ordre décroissant de puissance:  
As (A) : 4 cartes      
Roi (K) : 4 cartes    
Dame (Q) : 4 cartes    
Valet (J) : 4 cartes   
10 : 4 cartes  
9 : 4 cartes   
8 : 4 cartes   
7 : 4 cartes  
6 : 4 cartes  
5 : 4 cartes  
4 : 4 cartes  
3 : 4 cartes   
2 : 4 cartes  
## modelisation des cartes
un tableau taille = 52 chaque carte est codée par un entier de 1 à 14, la carte la plus puissante est celle avec le numéro le plus grand 
## Règles du jeu du projet : 
Le jeu de cartes (52 cartes) est distribue entièrement entre les deux joueurs de manière aléatoire, ils peuvent regarder leur carte tout au long du jeu
Le jeu continue jusqu'à que l'un des joueurs n'ait plus de carte
Il se repartit sous forme de manche: 
Les deux joueurs choisissent une carte à jouer de leur main
Ils les placent sur le terrain ; le joueur qui a la carte la plus forte gagne les 2 cartes et stocke ses cartes gagnees dans un tas d'attente
En cas d'egalité, les deux joueurs choisissent deux autres cartes a mettre en 'sacrifice' avant de rejouer avec deux nouvelles cartes (choisies) ; le gagnant gagne les 6 cartes. En cas d'egalité encore une fois, on continue à empiler les cartes jusqu´un joueur se departage.
Si un joueur arrive a la fin de ses cartes, son tas d'attente devient sa nouvelle main.
Le premier joueur qui arrive pour la 3e fois a son tas d'attente a perdu

## Solution
En utilisant la stratégie qui combine le choix de la carte la plus puissante pour affronter et le choix de la carte la plus faible en cas d draw permet au joueur 2 de gagner à chaque fois

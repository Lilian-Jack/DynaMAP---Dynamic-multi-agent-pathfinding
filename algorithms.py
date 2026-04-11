#Fichier pour les algorithme de traitement de graphe
import numpy as np
#importation de Queue car utiliser les listes python nous oblige à utiliser pop qui est en O(n) tandis que get est en 0(1)
from queue import Queue
from graph import  Grille


#Algorithme de parcours en largeur : Breadth First Search, permet de savoir si un point est atteignable à partir d'un autre point
def BFS(grille,x,y,xDest,yDest):
    f = Queue()
    #set() car savoir si un élément est dans set est en 0(1)
    marque = set()
    f.put((x,y))
    marque.add((x,y))
    while(not f.empty()):
        s = f.get()
        if(s[0]==xDest and s[1]==yDest):
            return True
        voisins = grille.voisins(s[0],s[1])
        for v in voisins:
            if v not in marque:
                f.put(v)
                marque.add(v)
    #On returne faux si on a exploré tout les destinations possible sans atteindre celle qu'on cherchait
    return False






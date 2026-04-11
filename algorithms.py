#Fichier pour les algorithme de traitement de graphe
import numpy as np
#heapq nous permet d'implémenter des files avec priorités
import heapq
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

#distance de manhattan plus adapté pour les chemins en forme de grille
def distanceManhattan(x,y,xP,yP):
    return (np.abs(x - xP) + np.abs(y - yP))

#fonction qui permet de construire le chemin effectué par Astar
def reconstruction(chemins,spawn,destination):
    chemin = []
    case = destination
    while case != spawn :
        chemin.append(case)
        case = chemins[case]
    chemin.reverse()
    return chemin

# Algorithme A* qui va nous permettre de déterminer les chemin de nos robots sur la grille
def Astar(grille,x,y,xDest,yDest):
    #case déjà exploré par l'algo pour ne pas tourner en rond (set() suffit)
    caseExplore = set()
    #case qu'on doit exploré
    caseNonExplore = []

    #dictionnaire qui garde en mémoire le cout des cases (le nombre de pas depuis le spawn)
    cout = {}
    heapq.heappush(caseNonExplore,(0,(x,y)))
    cout[(x,y)]=0

    #dictionnaire qui nous permet de retracer le chemin à la fin, clé : case ,valeur : case précédente
    chemins = {}
    #tant qu'on a pas exploré toutes les cases possibles
    while(caseNonExplore):
        u = heapq.heappop(caseNonExplore)
        #on regarde si la case est la destination
        if u[1][0]==xDest and u[1][1]==yDest:
            #fonction pour reconstituer le chemin
            chemin = reconstruction(chemins,(x,y),(xDest,yDest))

            return chemin
        voisins = grille.voisins(u[1][0],u[1][1])
        for v in voisins:
            vCout = cout[u[1]] + 1
            #on regarde si v n'est pas exploré ou exploré avec un coup supérieur
            if (v not in caseExplore) or (vCout<cout[v]):
                cout[v]=vCout
                vHeuristique = vCout + distanceManhattan(v[0],v[1],xDest,yDest)
                heapq.heappush(caseNonExplore,(vHeuristique,v))
                #construction du chemin
                chemins[v]=u[1]
        caseExplore.add(u[1])







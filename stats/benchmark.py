from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np
from implementation.instance import Instance
from algorithms.conflicts import detectionConflits
#fonctions pour comparer le nombre de conflits en fonctions des différentes variables de l'algorithme (taille grille,nb robots, densité d'obstacles)

#fonction qui défini le nombre de conflits en fonction de la taille de la grille avec densité et nbrobots fixé
def nbConflitsTailleGrille(densite,nbRobots):
    #on prend 20 iterations par état pour avoir une moyenne réaliste
    iterations = 50
    #tableau des différentes taille de grille
    tailles = np.arange(8,21,1)
    nb_conflits = []
    for taille in tailles:
        #moyenne des différentes itérations
        moyenne = 0
        for i in range(iterations):
            instance = Instance(taille,densite,nbRobots,"naif")
            detectionConflits(instance)
            nbConflit = len(instance.conflits_arretes) + len(instance.conflits_sommets)
            moyenne = moyenne + nbConflit
        moyenne = moyenne / iterations
        nb_conflits.append(moyenne)
        print(f"{moyenne} pour {taille} taille")

    plt.plot(tailles,nb_conflits,"r")
    plt.xlabel("Taille de la grille")
    plt.ylabel("Nombres de conflits")
    plt.title(f"Nombres de conflits en fonction de la taille de la grille \n densite : {densite} et nombre de robots : {nbRobots}")
    plt.tight_layout()
    plt.savefig('taille.png')
    plt.show()


#fonction qui défini le nombre de conflits en fonction du nombre de robots avec densité et taille de grille fixé
def nbConflitsNbRobots(densite,taille):
    iterations = 50
    nbRobots = np.arange(4,17,2)
    nb_conflits = []
    for nbRobot in nbRobots:
        moyenne = 0
        for i in range(iterations):
            instance = Instance(taille,densite,nbRobot,"naif")
            detectionConflits(instance)
            nbConflit = len(instance.conflits_arretes) + len(instance.conflits_sommets)
            moyenne = moyenne + nbConflit
        moyenne = moyenne / iterations
        nb_conflits.append(moyenne)
        print(f"{moyenne} pour {nbRobots} robots")
    plt.plot(nbRobots, nb_conflits, "b")
    plt.xlabel("Nombre de robots")
    plt.ylabel("Nombres de conflits")
    plt.title(f"Nombres de conflits en fonction du nombres de robots \n densite : {densite} et taille de grille : {taille}")
    plt.tight_layout()
    plt.savefig('NbRobots.png')
    plt.show()


#fonction qui défini le nombre de conflits en fonction de la densité avec nombre de robot fixé et taille de grille fixé
def nbConflitsDensite(nbRobot,taille):
    iterations = 50
    densites = [0,0.10,0.15,0.20,0.25,0.30,0.35]
    nb_conflits = []
    for densite in densites :
        moyenne = 0
        for i in range(iterations):
            instance = Instance(taille,densite,nbRobot,"naif")
            detectionConflits(instance)
            nbConflit = len(instance.conflits_arretes) + len(instance.conflits_sommets)
            moyenne = moyenne + nbConflit
        moyenne = moyenne / iterations
        nb_conflits.append(moyenne)
        print(f"{moyenne} pour {densite} de densité d'obstacles")
    plt.plot(densites, nb_conflits, "g")
    plt.xlabel("Densité de la grille")
    plt.ylabel("Nombres de conflits")
    plt.title(f"Nombres de conflits en fonction de la densité de la grille \n nombre de robots : {nbRobot} et taille de grille : {taille}")
    plt.tight_layout()
    plt.savefig('densite.png')
    plt.show()

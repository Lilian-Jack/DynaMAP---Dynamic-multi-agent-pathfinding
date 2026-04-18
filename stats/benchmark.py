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


#on va maintenant voir l'évolution de la longueur des chemins pour naif et ST en fonction des trois parametres
def CheminTailleGrille(nbRobot,densite):
    iterations = 50
    tailles = np.arange(10, 16, 1)
    longueur_naif = []
    longueur_ST = []
    for taille in tailles:
        moyenne_naif = 0
        moyenne_ST = 0
        for i in range(iterations):
            #on veut des instances ST sans robot qui n'ont pas trouvé leurs chemin, sinon ça fausse les métriques
            while(True):
                seed = np.random.randint(0, 10000)
                instance_naif = Instance(taille, densite, nbRobot, "naif", seed)
                instance_ST = Instance(taille,densite,nbRobot,"ST",seed)
                if not instance_ST.grille.isFailed():
                    break
            moyenne_naif += instance_naif.longueurMoyenneChemin()
            moyenne_ST += instance_ST.longueurMoyenneChemin()
        moyenne_naif = moyenne_naif / iterations
        moyenne_ST = moyenne_ST / iterations
        longueur_naif.append(moyenne_naif)
        longueur_ST.append(moyenne_ST)

    plt.plot(tailles,longueur_naif,"b",label="Astar")
    plt.plot(tailles,longueur_ST,"r",label="AstarST")
    plt.xlabel("taille de la grille")
    plt.ylabel("longueur des chemins")
    plt.title(f"longueur des chemins en fonction de la longueur de la grille \n nombres de robots : {nbRobot} et densite : {densite}")
    plt.legend()
    plt.savefig('chemin_taille.png')
    plt.show()

def CheminTailleNbRobots(taille,densite):
    iterations = 50
    nbRobots = np.arange(2, 20, 1)
    longueur_naif = []
    longueur_ST = []
    for nbRobot in nbRobots:
        moyenne_naif = 0
        moyenne_ST = 0
        for i in range(iterations):
            #on veut des instances ST sans robot qui n'ont pas trouvé leurs chemin, sinon ça fausse les métriques
            while(True):
                seed = np.random.randint(0, 10000)
                instance_naif = Instance(taille, densite, nbRobot, "naif", seed)
                instance_ST = Instance(taille,densite,nbRobot,"ST",seed)
                if not instance_ST.grille.isFailed():
                    break

            moyenne_naif += instance_naif.longueurMoyenneChemin()
            moyenne_ST += instance_ST.longueurMoyenneChemin()

        moyenne_naif = moyenne_naif / iterations
        moyenne_ST = moyenne_ST / iterations
        longueur_naif.append(moyenne_naif)
        longueur_ST.append(moyenne_ST)

    plt.plot(nbRobots,longueur_naif,"b",label="Astar")
    plt.plot(nbRobots,longueur_ST,"r",label="AstarST")
    plt.xlabel("Nombre de robots")
    plt.ylabel("longueur des chemins")
    plt.title(f"longueur des chemins en fonction de la longueur du nombres de robots \n taille de la grille : {taille} et densite : {densite}")
    plt.legend()
    plt.savefig('chemin_nbRobot.png')
    plt.show()

def CheminTailleDensite(taille,nbRobot):
    iterations = 50
    densites = [0,0.10,0.15,0.20,0.25,0.30,0.35]
    longueur_naif = []
    longueur_ST = []
    for densite in densites:
        moyenne_naif = 0
        moyenne_ST = 0
        for i in range(iterations):
            #on veut des instances ST sans robot qui n'ont pas trouvé leurs chemin, sinon ça fausse les métriques
            while(True):
                seed = np.random.randint(0, 10000)
                instance_naif = Instance(taille, densite, nbRobot, "naif", seed)
                instance_ST = Instance(taille,densite,nbRobot,"ST",seed)
                if not instance_ST.grille.isFailed():
                    break

            moyenne_naif += instance_naif.longueurMoyenneChemin()
            moyenne_ST += instance_ST.longueurMoyenneChemin()

        moyenne_naif = moyenne_naif / iterations
        moyenne_ST = moyenne_ST / iterations
        longueur_naif.append(moyenne_naif)
        longueur_ST.append(moyenne_ST)

    plt.plot(densites,longueur_naif,"b",label="Astar")
    plt.plot(densites,longueur_ST,"r",label="AstarST")
    plt.xlabel("Densite de la grille")
    plt.ylabel("longueur des chemins")
    plt.title(f"longueur des chemins en fonction de la longueur de la densite d'obstacles \n taille de la grille : {taille} et nombres de robots: {nbRobot}")
    plt.legend()
    plt.savefig('chemin_densite.png')
    plt.show()

def attentesNbRobots(taille, densite):
    iterations = 50
    nbRobots = np.arange(10, 21, 1)
    nb_attentes = []

    for nbRobot in nbRobots:
        moyenne_attente = 0

        for i in range(iterations):
            instance = Instance(taille, densite, nbRobot, "ST")
            moyenne_attente += instance.grille.nbAttentes()

        moyenne_attente = moyenne_attente / iterations
        nb_attentes.append(moyenne_attente)

    plt.plot(nbRobots, nb_attentes, "r")

    plt.xlabel("Nombre de robots")
    plt.ylabel("Nombre d'attentes")
    plt.title("Nombre d'attentes en fonction du nombre de robots")

    plt.savefig("attente.png")
    plt.show()

#DynaMAP - Dynamic multi agent Pathfinding
import numpy as np
from graph import Grille, Robot
from algorithms import BFS





#Fonction qui permet de crée différentes instance de grille avec des robots
def createInstance(taille,partObstacle,nbRobot):
    grille = Grille(taille,partObstacle)

    # Création d'un tableau avec des couleurs aléatoires
    colors = ['#%06X' % np.random.randint(0, 0xFFFFFF) for i in range(nbRobot)]

    #Création des robots
    for i in range(nbRobot):

        #pour chaque robot on crée un spawn et une destinations sur une case vide / while(true) + break = équivalent do while
        while(True):
            x = np.random.randint(0,taille-1)
            y = np.random.randint(0,taille-1)
            while(grille.occupe(x,y)):
                x = np.random.randint(0, taille - 1)
                y = np.random.randint(0, taille - 1)

            xDest = np.random.randint(0,taille-1)
            yDest = np.random.randint(0,taille-1)
            while(grille.occupe(xDest,yDest) or (xDest == x and yDest == y)):
                xDest = np.random.randint(0,taille - 1)
                yDest = np.random.randint(0,taille - 1)


            # nécessité de regarder si la destination du robot est atteignable depuis son spawn
            if(BFS(grille,x,y,xDest,yDest)):
                robot = Robot(i, x, y, xDest, yDest, colors[i])
                # on ajoute les robots dans la grille
                grille.ajoutRobot(robot)
                break

    return grille


grilleTest = createInstance(25,0.15,3)
grilleTest.afficheGrille()






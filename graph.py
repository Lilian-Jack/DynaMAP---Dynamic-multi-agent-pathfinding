import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


#classe robot qui va bouger sur la grille, statut indique si le robot est arrivé à sa destination
class Robot:
    def __init__(self,id,x,y,xFinal,yFinal,couleur):
        self.id = id
        self.x = x
        self.y = y
        self.xFinal = xFinal
        self.yFinal = yFinal
        self.statut = False
        self.couleur = couleur
        self.chemin = []
    def ajoutChemin(self):
        self.chemin.append((self.x,self.y))

#class Grille qui permet de construire des grilles
class Grille:
    def __init__(self,taille,partObstacle):
        self.taille = taille
        self.partObstacle = partObstacle
        self.grille =  np.random.choice([True, False], size=(taille, taille), p=[partObstacle, 1-partObstacle])
        self.robots = []

    def ajoutRobot(self,robot):
        self.robots.append(robot)

    #occupe permet de placer les spawns et les destinations à des endroits non occupé par des obstacles, des spawns ou des destinations
    def occupe(self,x,y):
        if(self.grille[x][y] == True):
            return True
        else:
            for robot in self.robots:
                if((robot.x == x and robot.y == y) or (robot.xFinal == x and robot.yFinal == y)):
                    return True
        return False

    #voisin permet de trouver les voisins d'une case non occupé par un obstacle
    def voisins(self,x,y):
        potentiels_voisins = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        voisins = []
        for i,j in potentiels_voisins:
            if (i >= 0 and i<self.taille and j>=0 and j<self.taille and not self.grille[i][j]):
                voisins.append((i,j))
        return voisins

    #methode qui permet d'afficher l'état de la grille
    def afficheGrille(self):
        #blanc pour le vide et gris pour les murs
        cmap = ListedColormap(["white","grey"])

        #Création de la grille de valeur
        grilleAffichage = np.full((self.taille,self.taille),0)

        for robot in self.robots:
            #Affichage des spawns avec o
            plt.plot(robot.y, robot.x, marker='o', color=robot.couleur,markersize=10, markeredgecolor='black', markeredgewidth=1.5)
            #Affichage des destinations avec *
            plt.plot(robot.yFinal, robot.xFinal, marker='*', color=robot.couleur,markersize=12, markeredgecolor='black', markeredgewidth=1.5)

        #On applique le maste booléen pour placer les obstacles
        grilleAffichage[self.grille] = 1

        plt.imshow(grilleAffichage,cmap=cmap)
        plt.show()










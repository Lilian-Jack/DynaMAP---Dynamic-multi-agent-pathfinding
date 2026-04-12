import numpy as np
from graph import Grille, Robot
from algorithms import BFS, Astar
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

#class qui permet des crées des instances facilement
class Instance:
    def __init__(self,taille,partObstacle,nbRobot):
        #Fonction qui permet de crée différentes instance de grille avec des robots
        self.grille = Grille(taille,partObstacle)

        # Création d'un tableau avec des couleurs aléatoires
        colors = ['#%06X' % np.random.randint(0, 0xFFFFFF) for i in range(nbRobot)]

        #Création des robots
        for i in range(nbRobot):

            #pour chaque robot on crée un spawn et une destinations sur une case vide / while(true) + break = équivalent do while
            while(True):
                x = np.random.randint(0,taille-1)
                y = np.random.randint(0,taille-1)
                while(self.grille.occupe(x,y)):
                    x = np.random.randint(0, taille - 1)
                    y = np.random.randint(0, taille - 1)

                xDest = np.random.randint(0,taille-1)
                yDest = np.random.randint(0,taille-1)
                while(self.grille.occupe(xDest,yDest) or (xDest == x and yDest == y)):
                    xDest = np.random.randint(0,taille - 1)
                    yDest = np.random.randint(0,taille - 1)


                # nécessité de regarder si la destination du robot est atteignable depuis son spawn
                if(BFS(self.grille,x,y,xDest,yDest)):
                    robot = Robot(i, x, y, xDest, yDest, colors[i])
                    robot.chemin = Astar(self.grille,x,y,xDest,yDest)
                    # on ajoute les robots dans la grille
                    self.grille.ajoutRobot(robot)
                    break

    #methode qui permet d'afficher l'état de la grille
    def afficheGrille(self):
        #blanc pour le vide et gris pour les murs
        cmap = ListedColormap(["white","grey"])

        #Création de la grille de valeur
        grilleAffichage = np.full((self.grille.taille,self.grille.taille),0)

        for robot in self.grille.robots:
            #Affichage des spawns avec o
            plt.plot(robot.y, robot.x, marker='o', color=robot.couleur,markersize=10, markeredgecolor='black', markeredgewidth=1.5)
            #Affichage des destinations avec *
            plt.plot(robot.yFinal, robot.xFinal, marker='*', color=robot.couleur,markersize=12, markeredgecolor='black', markeredgewidth=1.5)

        #On applique le maste booléen pour placer les obstacles
        grilleAffichage[self.grille.grille] = 1

        #permet de faire un quadrillage ticks permet de décaler les lignespour qu'elles s'alignent sur les cases
        plt.xticks(np.arange(-0.5, self.grille.taille, 1), [])
        plt.yticks(np.arange(-0.5, self.grille.taille, 1), [])
        plt.grid(True, color='black', linewidth=0.5)

        plt.imshow(grilleAffichage,cmap=cmap)
        plt.show()

    #méthode pour animer les différentes frame
    def animer(self):
        #nombre de frame total = chemin le plus long
        nbFrame = max(len(robot.chemin) for robot in self.grille.robots)
        cmap = ListedColormap(["white","grey"])
        fig, ax = plt.subplots(figsize=(6,6), dpi=200)

        #on veut garder le point de départ afficher

        #fonction update appelé à chaque frame
        def update(frame):
            ax.clear()

            grilleAffichage = np.full((self.grille.taille, self.grille.taille), 0)
            grilleAffichage[self.grille.grille] = 1
            ax.imshow(grilleAffichage, cmap=cmap)

            ax.set_xticks(np.arange(-0.5, self.grille.taille, 1), [])
            ax.set_yticks(np.arange(-0.5, self.grille.taille, 1), [])
            ax.grid(True, color='black', linewidth=0.5)

            for robot in self.grille.robots:
                if frame < len(robot.chemin):
                    robot.x, robot.y = robot.chemin[frame]
                #spawn
                ax.plot(robot.ySpawn, robot.xSpawn, marker='o', color=robot.couleur, markersize=10, markeredgecolor='black',markeredgewidth=1.5)
                #destination
                ax.plot(robot.yFinal, robot.xFinal, marker="*", color=robot.couleur,markersize=12, markeredgecolor='black', markeredgewidth=1.5)
                #emplacement
                ax.plot(robot.y, robot.x, marker=".", color=robot.couleur,markersize=10, markeredgecolor='black', markeredgewidth=1.5)

        anime = FuncAnimation(fig,update,frames=nbFrame,interval=200)
        anime.save("anime.gif",writer="pillow",fps=2)







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
        #Va nous permettre de savoir ou sont les conflit si des robots réserves les mêmes noeuds ou arretes
        self.reservations_noeuds = {}
        self.reservations_arretes = {}
        self.conflits_sommets = {}
        self.conflits_arretes = {}
        conflits_arretes = {}
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
    #fonction qui nous permet de déterminer les conflits entre agents
    def detectionConflits(self):
        for robot in self.grille.robots:
            #Détection des conflits sur les noeuds
            for t, (x,y) in enumerate(robot.chemin):
                if (x,y,t) not in self.reservations_noeuds:
                    self.reservations_noeuds[(x,y,t)] = []
                self.reservations_noeuds[(x, y, t)].append(robot.id)
            #Détection des conflits sur les arrêtes
            for t in range(len(robot.chemin)-1):
                x1,y1 = robot.chemin[t]
                x2,y2 = robot.chemin[t+1]
                if (x1,y1,x2,y2,t) not in self.reservations_arretes:
                    self.reservations_arretes[(x1,y1,x2,y2,t)] = []
                self.reservations_arretes[(x1,y1,x2,y2,t)].append(robot.id)

        conflits_sommets = {}
        conflits_arretes = {}

        # Enumération des différents conflits
        for key, value in self.reservations_noeuds.items():
            if len(value) > 1:
                conflits_sommets[key] = value

        for (x1, y1, x2, y2, t), value in self.reservations_arretes.items():
            if (x2, y2, x1, y1, t) in self.reservations_arretes.keys() and (x2, y2, x1, y1,t) not in conflits_arretes.keys():
                conflits_arretes[(x1, y1, x2, y2, t)] = value + self.reservations_arretes[(x2, y2, x1, y1, t)]

        print("Il y a " + str(len(conflits_sommets)) + " vertex conflicts dans cette instance :")
        for (x, y, t), value in conflits_sommets.items():
            print("Conflit en (" + str(x) + "," + str(y) + ") à " + str(t) + " entre les agents : " + str(value))

        print("Il y a " + str(len(conflits_arretes)) + " edges conflicts dans cette instance :")
        for (x1, y1, x2, y2, t), value in conflits_arretes.items():
            print("Conflit en (" + str(x1) + "," + str(y1) + "," + str(x2) + "," + str(y2) + ") à " + str(
                t) + " entre les agents : " + str(value))

        self.conflits_arretes = conflits_arretes
        self.conflits_sommets = conflits_sommets



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
        cmap = ListedColormap(["white","grey","red"])
        fig, ax = plt.subplots(figsize=(6,6), dpi=200)

        #on veut garder le point de départ afficher

        #fonction update appelé à chaque frame
        def update(frame):
            ax.clear()

            grilleAffichage = np.full((self.grille.taille, self.grille.taille), 0)
            grilleAffichage[self.grille.grille] = 1

            #affichage des conflits
            for (x1,y1,t) in self.conflits_sommets.keys():
                if t==frame:
                    grilleAffichage[x1,y1]=2
            for (x1, y1, x2, y2, t) in self.conflits_arretes.keys():
                if t==frame:
                    grilleAffichage[x1,y1]=2
                    grilleAffichage[x2,y2]=2
            ax.imshow(grilleAffichage, cmap=cmap, vmin=0, vmax=2)

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







import numpy as np
from implementation.graph import Grille, Robot
from algorithms.Astar import Astar,BFS,AstarST

#class qui permet des crées des instances facilement
class Instance:
    def __init__(self,taille,partObstacle,nbRobot,mode,seed=None):
        if seed is not None:
            np.random.seed(seed)
        #Fonction qui permet de crée différentes instance de grille avec des robots
        self.grille = Grille(taille,partObstacle)
        #Va nous permettre de savoir ou sont les conflit si des robots réserves les mêmes noeuds ou arretes
        self.reservations_noeuds = {}
        self.reservations_arretes = {}
        self.conflits_sommets = {}
        self.conflits_arretes = {}
        self.mode = mode
        # Création d'un tableau avec des couleurs aléatoires
        colors = ['#%06X' % np.random.randint(0, 0xFFFFFF) for i in range(nbRobot)]

        #Création des robots
        for i in range(nbRobot):

            #pour chaque robot on crée un spawn et une destinations sur une case vide / while(true) + break = équivalent do while
            while(True):
                x = np.random.randint(0,taille)
                y = np.random.randint(0,taille)
                while(self.grille.occupe(x,y)):
                    x = np.random.randint(0, taille)
                    y = np.random.randint(0, taille)

                xDest = np.random.randint(0,taille)
                yDest = np.random.randint(0,taille)
                while(self.grille.occupe(xDest,yDest) or (xDest == x and yDest == y)):
                    xDest = np.random.randint(0,taille)
                    yDest = np.random.randint(0,taille)

                # nécessité de regarder si la destination du robot est atteignable depuis son spawn
                if(BFS(self.grille,x,y,xDest,yDest)):

                    if self.mode == "naif":
                        chemin = Astar(self.grille,x,y,xDest,yDest)
                    elif self.mode == "ST":
                        chemin = AstarST(self.grille,x,y,xDest,yDest)

                    robot = Robot(i, x, y, xDest, yDest, colors[i])
                    if chemin is None :
                        print(f"[Warning] : Robot {i} : aucun chemin trouvé")
                        robot.failed = True
                        robot.chemin = []
                    else :
                        robot.chemin = chemin
                    # on ajoute les robots dans la grille
                    self.grille.ajoutRobot(robot)
                    #fin du while
                    break











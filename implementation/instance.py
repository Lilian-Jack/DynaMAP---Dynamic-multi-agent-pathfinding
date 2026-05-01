import numpy as np
from implementation.graph import Grille, Robot
from algorithms.Astar import Astar,BFS,AstarST
from implementation.CBS import CBS
#class qui permet des crées des instances facilement
class Instance:
    def __init__(self, taille, partObstacle, nbRobot, mode, seed=None):
        if seed is not None:
            np.random.seed(seed)
        #Fonction qui permet de crée différentes instance de grille avec des robots
        self.grille = Grille(taille, partObstacle)
        #Va nous permettre de savoir ou sont les conflit si des robots réserves les mêmes noeuds ou arretes
        self.reservations_noeuds = {}
        self.reservations_arretes = {}

        self.conflits_sommets = {}
        self.conflits_arretes = {}
        self.mode = mode
        #Création d'un tableau avec des couleurs aléatoires
        colors = ['#%06X' % np.random.randint(0, 0xFFFFFF) for i in range(nbRobot)]

        #Création des robots
        for i in range(nbRobot):
            #pour chaque robot on crée un spawn et une destinations sur une case vide / while(true) + break = équivalent do while
            while True:
                x = np.random.randint(0, taille)
                y = np.random.randint(0, taille)
                while self.grille.occupe(x, y):
                    x = np.random.randint(0, taille)
                    y = np.random.randint(0, taille)

                xDest = np.random.randint(0, taille)
                yDest = np.random.randint(0, taille)
                while self.grille.occupe(xDest, yDest) or (xDest == x and yDest == y):
                    xDest = np.random.randint(0, taille)
                    yDest = np.random.randint(0, taille)

                #nécessité de regarder si la destination du robot est atteignable depuis son spawn
                if BFS(self.grille, x, y, xDest, yDest):
                    robot = Robot(i, x, y, xDest, yDest, colors[i])
                    self.grille.ajoutRobot(robot)
                    break

        #calcul des chemins en fonction du mode
        if self.mode == "naif":
            for robot in self.grille.robots:
                chemin = Astar(self.grille, robot.xSpawn, robot.ySpawn, robot.xFinal, robot.yFinal)
                if chemin is None:
                    robot.failed = True
                    robot.chemin = []
                else:
                    robot.chemin = chemin

        elif self.mode == "ST":
            for robot in self.grille.robots:
                chemin = AstarST(self.grille, robot.xSpawn, robot.ySpawn, robot.xFinal, robot.yFinal)
                if chemin is None:
                    robot.failed = True
                    robot.chemin = []
                else:
                    robot.chemin = chemin

        elif self.mode == "CBS":
            cbs = CBS(self.grille)
            solutions = cbs.resoudre()
            if solutions is not None:
                for robot in self.grille.robots:
                    chemin = solutions[robot.id]
                    if chemin is None:
                        robot.failed = True
                        robot.chemin = []
                    else:
                        robot.chemin = chemin
            else:
                print("[Warning] CBS n'a pas trouvé de solution")
                for robot in self.grille.robots:
                    robot.failed = True
                    robot.chemin = []

    # fonction qui va calculer la longueur moyenne des chemins dans une instance
    def longueurMoyenneChemin(self):
        moyenne = 0
        for robot in self.grille.robots:
            if robot.chemin != []:
                moyenne += len(robot.chemin)
        moyenne = moyenne / len(self.grille.robots)
        return moyenne












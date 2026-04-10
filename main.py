#DynaMAP - Dynamic multi agent Pathfinding
import numpy as np

#class Grille qui permet de construire des grilles
class Grille:
    def __init__(self,taille,partObstacle):
        self.taille = taille
        self.partObstacle = partObstacle
        self.grille =  np.random.choice([True, False], size=(taille, taille), p=[partObstacle, 1-partObstacle])
        self.robots = []

    def ajoutRobot(self,robot):
        self.robots.append(robot)
    def occupe(self,x,y):
        if(self.grille[x][y] == True):
            return True
        else:
            for robot in self.robots:
                if((robot.x == x and robot.y == y) or (robot.xFinal == x and robot.yFinal == y)):
                    return True
        return False


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




#Création d'un tableau avec des couleurs aléatoires
colors = ['#%06X' % np.random.randint(0, 0xFFFFFF) for i in range(100)]

#Fonction qui permet de crée différentes instance de grille avec des robots
def createInstance(taille,partObstacle,nbRobot):
    grille = Grille(taille,partObstacle)

    #Création des robots
    for i in range(nbRobot):

        #pour chaque robot on crée un spawn et une destinations sur une case vide
        x = np.random.randint(0,taille-1)
        y = np.random.randint(0,taille-1)
        while(grille.occupe(x,y)):
            x = np.random.randint(0, taille - 1)
            y = np.random.randint(0, taille - 1)
        grille.ajoutSpawn(x,y)

        xDest = np.random.randint(0,taille-1)
        yDest = np.random.randint(0,taille-1)
        while(grille.occupe(xDest,yDest)):
            xDest = np.random.randint(0,taille - 1)
            yDest = np.random.randint(0,taille - 1)
        grille.ajoutDestination(xDest,yDest)

        robot = Robot(i,x,y,xDest,yDest,colors[i])

        #nécessité de regarder si la destination du robot est atteignable depuis son spawn
        #on ajoute les robots dans la grille
        grille.ajoutRobot(robot)




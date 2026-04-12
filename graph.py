import numpy as np




#classe robot qui va bouger sur la grille, statut indique si le robot est arrivé à sa destination
class Robot:
    def __init__(self,id,x,y,xFinal,yFinal,couleur):
        self.id = id
        self.x = x
        self.y = y
        self.xSpawn=x
        self.ySpawn=y
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












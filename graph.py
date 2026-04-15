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
        self.time = 0
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

    #fonction voisins qui va prendre en compte le contexte spatio-temporel qui permettra d'éliminer les conflits, rajout de la possibilité de faire du surplace
    def voisinsST(self,x,y,t):
        potentiels_voisins = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),(x,y)]
        voisins = []
        t_suivant = t +1
        for i,j in potentiels_voisins:
            potentiel = True
            if (i >= 0 and i<self.taille and j>=0 and j<self.taille and not self.grille[i][j]):
                for robot in self.robots:
                    #condition qui empêche de prendre une case déjà occupe (1er condition vérifie le vertex conflitc et 2eme le edge conflict)
                    if t_suivant < len(robot.chemin):
                        #on regarde si la case est occupé à la prochaine itération
                        if robot.chemin[t_suivant]==(i,j):
                            potentiel = False
                            break
                        if robot.chemin[t]==(i,j) and robot.chemin[t_suivant]==(x,y):
                            potentiel = False
                            break
                    #on prend en compte le fait qu'il y ai des robots déjà arrivé à destination
                    else:
                        if robot.chemin[-1]==(i,j):
                            potentiel = False

            if potentiel :
                voisins.append((i, j))

        return voisins











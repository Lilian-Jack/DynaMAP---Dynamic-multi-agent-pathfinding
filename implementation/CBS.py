from implementation.graph import Grille
from algorithms.Astar import AstarCBS

#class noeud CBS qui sera stocké dans une file de priorité puis traité jusqu'à tomber sur un noeud sans
class noeudCBS:
    def __init__(self,grille,contraintes):
        self.contraintes = contraintes
        self.solutions = {}
        self.cout = 0

        
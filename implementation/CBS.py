from implementation.graph import Grille
from algorithms.Astar import AstarCBS
import heapq
# class noeud CBS qui sera stocké dans une file de priorité puis traité jusqu'à tomber sur un noeud sans conflit
class NoeudCBS:
    def __init__(self, grille, contraintes):
        self.contraintes = contraintes
        self.solutions = {}
        self.cout = 0

        # on va recalculer le chemin pour chaque robot avec leurs contraintes
        for robot in grille.robots:
            contraintes_robot = {(x, y, t) for (rid, x, y, t) in contraintes if rid == robot.id}
            chemin = AstarCBS(grille, robot.xSpawn, robot.ySpawn, robot.xFinal, robot.yFinal, contraintes_robot)
            self.solutions[robot.id] = chemin
            if chemin is not None:
                self.cout += len(chemin)
            else:
                # noeud invalide — ne sera jamais extrait de la file en premier
                self.cout = float('inf')
                break

    # fonction qui retourne le premier conflit trouvé, None si aucun conflit
    def premierConflit(self):
        ids = list(self.solutions.keys())
        max_frame = max(len(chemin) for chemin in self.solutions.values() if chemin is not None)

        for t in range(max_frame):
            for i in range(len(ids)):
                for j in range(i + 1, len(ids)):
                    idA = ids[i]
                    idB = ids[j]
                    cheminA = self.solutions[idA]
                    cheminB = self.solutions[idB]

                    # position à t ou dernière position si robot arrivé
                    posA = cheminA[t] if t < len(cheminA) else cheminA[-1]
                    posB = cheminB[t] if t < len(cheminB) else cheminB[-1]

                    # vertex conflict
                    if posA == posB:
                        return (idA, idB, posA[0], posA[1], t)

                    # edge conflict
                    if t + 1 < max_frame:
                        posA_next = cheminA[t + 1] if t + 1 < len(cheminA) else cheminA[-1]
                        posB_next = cheminB[t + 1] if t + 1 < len(cheminB) else cheminB[-1]

                        if posA == posB_next and posB == posA_next:
                            return (idA, idB, posA[0], posA[1], posB[0], posB[1], t)

        return None

    #fonctrion pour comparer deux noeud
    def __lt__(self, other):
        return self.cout < other.cout


# class CBS qui gère l'arbre de recherche et résout les conflits
class CBS:
    def __init__(self, grille):
        self.grille = grille
        self.arbre = []

    def resoudre(self):
        # création du noeud racine sans contraintes
        racine = NoeudCBS(self.grille, set())
        heapq.heappush(self.arbre, (racine.cout, racine))

        while self.arbre:
            #on récupére le noeud prioritaire
            _, noeud = heapq.heappop(self.arbre)

            conflit = noeud.premierConflit()

            if conflit is None:
                return noeud.solutions

            idA, idB = conflit[0], conflit[1]

            #on regarde si c'est un vertex conflit ou un edge conflict
            if len(conflit) == 5:
                x, y, t = conflit[2], conflit[3], conflit[4]
                contrainte_A = (idA,x,y,t)
                contrainte_B = (idB,x,y,t)
            else:
                x1, y1, x2, y2, t = conflit[2], conflit[3], conflit[4], conflit[5], conflit[6]
                contrainte_A = (idA, x1, y1, t)
                contrainte_B = (idB, x2, y2, t)


            contraintes_gauche = noeud.contraintes | {contrainte_A}
            fils_gauche = NoeudCBS(self.grille, contraintes_gauche)
            heapq.heappush(self.arbre, (fils_gauche.cout, fils_gauche))

            contraintes_droite = noeud.contraintes | {contrainte_B}
            fils_droit = NoeudCBS(self.grille, contraintes_droite)
            heapq.heappush(self.arbre, (fils_droit.cout, fils_droit))

        return None
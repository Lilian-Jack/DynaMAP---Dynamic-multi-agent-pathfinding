#DynaMAP - Dynamic multi agent Pathfinding
from implementation.instance import Instance
from algorithms.conflicts import detectionConflits
from visualization.animation import afficheGrille,animer
from stats.benchmark import *

"""
grilleTest = Instance(16,0.15,8,"naif",seed=98)
afficheGrille(grilleTest)
detectionConflits(grilleTest)
animer(grilleTest)
"""

#benchmark
"""

nbConflitsTailleGrille(0.15,12)
nbConflitsNbRobots(0.15,12)
nbConflitsDensite(12,12)

CheminTailleGrille(12,0.15)
CheminTailleNbRobots(12,0.15)
CheminTailleDensite(12,8)
#attentesNbRobots(10,0.15)
"""
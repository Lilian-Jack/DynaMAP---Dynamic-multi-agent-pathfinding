#DynaMAP - Dynamic multi agent Pathfinding
from implementation.instance import Instance
from algorithms.conflicts import detectionConflits
from visualization.animation import afficheGrille,animer
from stats.benchmark import *


grilleTest = Instance(8,0.15,10,"naif",seed=98)
afficheGrille(grilleTest)
detectionConflits(grilleTest)
animer(grilleTest)


"""
#benchmark
nbConflitsTailleGrille(0.15,12)
nbConflitsNbRobots(0.15,12)
nbConflitsDensite(12,12)
"""
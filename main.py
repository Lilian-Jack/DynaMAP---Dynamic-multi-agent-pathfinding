#DynaMAP - Dynamic multi agent Pathfinding
from implementation.instance import Instance
from algorithms.conflicts import detectionConflits
from visualization.animation import afficheGrille,animer

grilleTest = Instance(15,0.15,20,"ST",42)
afficheGrille(grilleTest)
detectionConflits(grilleTest)
animer(grilleTest)

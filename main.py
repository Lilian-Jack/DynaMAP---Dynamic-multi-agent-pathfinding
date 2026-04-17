#DynaMAP - Dynamic multi agent Pathfinding
from instance import Instance

#mode = ST ou naif
grilleTest = Instance(5,0.15,5,"naif",32)
grilleTest.afficheGrille()
grilleTest.detectionConflits()
grilleTest.animer()

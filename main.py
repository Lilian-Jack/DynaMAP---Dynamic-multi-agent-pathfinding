#DynaMAP - Dynamic multi agent Pathfinding
from instance import Instance

#mode = ST ou naif
grilleTest = Instance(10,0.15,4,"naif",45)
grilleTest.afficheGrille()
grilleTest.detectionConflits()
grilleTest.animer()






#fonction qui nous permet de déterminer les conflits entre agents
def detectionConflits(instance):
    for robot in instance.grille.robots:
        # Détection des conflits sur les noeuds
        for t, (x, y) in enumerate(robot.chemin):
            if (x, y, t) not in instance.reservations_noeuds:
                instance.reservations_noeuds[(x, y, t)] = []
            instance.reservations_noeuds[(x, y, t)].append(robot.id)
        # Détection des conflits sur les arrêtes
        for t in range(len(robot.chemin) - 1):
            x1, y1 = robot.chemin[t]
            x2, y2 = robot.chemin[t + 1]
            # on ignore le surplace
            if (x1, y1) == (x2, y2):
                continue
            if (x1, y1, x2, y2, t) not in instance.reservations_arretes:
                instance.reservations_arretes[(x1, y1, x2, y2, t)] = []
            instance.reservations_arretes[(x1, y1, x2, y2, t)].append(robot.id)

    conflits_sommets = {}
    conflits_arretes = {}

    # Enumération des différents conflits
    for key, value in instance.reservations_noeuds.items():
        if len(value) > 1:
            conflits_sommets[key] = value

    for (x1, y1, x2, y2, t), value in instance.reservations_arretes.items():
        if (x2, y2, x1, y1, t) in instance.reservations_arretes.keys() and (x2, y2, x1, y1,
                                                                        t) not in conflits_arretes.keys():
            conflits_arretes[(x1, y1, x2, y2, t)] = value + instance.reservations_arretes[(x2, y2, x1, y1, t)]

    print("Il y a " + str(len(conflits_sommets)) + " vertex conflicts dans cette instance :")
    for (x, y, t), value in conflits_sommets.items():
        print("Conflit en (" + str(x) + "," + str(y) + ") à " + str(t) + " entre les agents : " + str(value))

    print("Il y a " + str(len(conflits_arretes)) + " edges conflicts dans cette instance :")
    for (x1, y1, x2, y2, t), value in conflits_arretes.items():
        print("Conflit en (" + str(x1) + "," + str(y1) + "," + str(x2) + "," + str(y2) + ") à " + str(
            t) + " entre les agents : " + str(value))

    instance.conflits_arretes = conflits_arretes
    instance.conflits_sommets = conflits_sommets
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np
#methode qui permet d'afficher l'état de la grille
def afficheGrille(instance):
    # blanc pour le vide et gris pour les murs
    cmap = ListedColormap(["white", "grey"])

    # Création de la grille de valeur
    grilleAffichage = np.full((instance.grille.taille, instance.grille.taille), 0)

    for robot in instance.grille.robots:
        # Affichage des spawns avec o
        plt.plot(robot.y, robot.x, marker='o', color=robot.couleur, markersize=10, markeredgecolor='black',
                 markeredgewidth=1.5)
        # Affichage des destinations avec *
        plt.plot(robot.yFinal, robot.xFinal, marker='*', color=robot.couleur, markersize=12, markeredgecolor='black',
                 markeredgewidth=1.5)

    # On applique le maste booléen pour placer les obstacles
    grilleAffichage[instance.grille.grille] = 1

    # permet de faire un quadrillage ticks permet de décaler les lignespour qu'elles s'alignent sur les cases
    plt.xticks(np.arange(-0.5, instance.grille.taille, 1), [])
    plt.yticks(np.arange(-0.5, instance.grille.taille, 1), [])
    plt.grid(True, color='black', linewidth=0.5)

    plt.imshow(grilleAffichage, cmap=cmap)
    plt.show()


# méthode pour animer les différentes frame
def animer(instance):
    # nombre de frame total = chemin le plus long
    nbFrame = max(len(robot.chemin) for robot in instance.grille.robots)
    cmap = ListedColormap(["white", "grey", "red"])
    fig, ax = plt.subplots(figsize=(6, 6), dpi=200)

    # on veut garder le point de départ afficher

    # fonction update appelé à chaque frame
    def update(frame):
        ax.clear()

        grilleAffichage = np.full((instance.grille.taille, instance.grille.taille), 0)
        grilleAffichage[instance.grille.grille] = 1

        # affichage des conflits
        for (x1, y1, t) in instance.conflits_sommets.keys():
            if t == frame:
                grilleAffichage[x1, y1] = 2
        for (x1, y1, x2, y2, t) in instance.conflits_arretes.keys():
            if t == frame:
                grilleAffichage[x1, y1] = 2
                grilleAffichage[x2, y2] = 2
        ax.imshow(grilleAffichage, cmap=cmap, vmin=0, vmax=2)

        ax.set_xticks(np.arange(-0.5, instance.grille.taille, 1), [])
        ax.set_yticks(np.arange(-0.5, instance.grille.taille, 1), [])
        ax.grid(True, color='black', linewidth=0.5)

        for robot in instance.grille.robots:
            if frame < len(robot.chemin):
                robot.x, robot.y = robot.chemin[frame]
            # spawn
            ax.plot(robot.ySpawn, robot.xSpawn, marker='o', color=robot.couleur, markersize=10, markeredgecolor='black',
                    markeredgewidth=1.5)
            # destination
            ax.plot(robot.yFinal, robot.xFinal, marker="*", color=robot.couleur, markersize=12, markeredgecolor='black',
                    markeredgewidth=1.5)
            # emplacement
            ax.plot(robot.y, robot.x, marker=".", color=robot.couleur, markersize=10, markeredgecolor='black',
                    markeredgewidth=1.5)

    anime = FuncAnimation(fig, update, frames=nbFrame, interval=200)
    anime.save("anime.gif", writer="pillow", fps=2)
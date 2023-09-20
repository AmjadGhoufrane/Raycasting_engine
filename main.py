import pygame
import sys
import math
from parametres import *
from carte import *
from joueur import *
from raycaster import *
from pygame.locals import *
from chargeur_textures import *
from processeur_objets import *

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()


class Mainlanceur:
    def __init__(self, xd_lc, yd_lc):
        self.delta_time = 1
        self.fenetre = pygame.display.set_mode((xd_lc, yd_lc))
        self.continuer = True
        self.clock = pygame.time.Clock()
        self.carte = Carte(self)
        self.renderer = renderer(self)
        self.joueur = Joueur(self)
        self.raycasteur = raycasteur(self)
        self.sprite = Processeur(self)
        self.Main()

    def Main(self):
        pygame.mouse.set_visible(False)
        self.clock.tick(FPS)
        pygame.display.set_caption(
            f'{self.clock.get_fps():.1f}' + '        ' + 'x = ' + f'{self.joueur.x:.1f}' + '  ' + 'y = ' + f'{self.joueur.y:.1f}')  # Permet d'afficher les fps en live à la place du nom de la fenetre
        self.raycasteur.update()
        self.sprite.update()
        self.joueur.update()
        self.renderer.draw()
        pygame.draw.rect(self.fenetre, 'black', pygame.Rect(0, -260, 520, 520))
        self.carte.draw()
        self.joueur.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
                pygame.mouse.set_visible(True)
                self.continuer = False


jeu = Mainlanceur(xd,yd)

while jeu.continuer:
    jeu.Main()

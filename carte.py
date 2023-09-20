import pygame

_ = False


class Carte:
    def __init__(self, jeu):
        self.jeu = jeu
        self.carte = [
#  1       2       3       4       5       6       7       8       9      10      11      12      13      14      15      16      17      18      19      20      22      23      24      25      26      27
[1,     1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1],
[1,     _,      _,      _,      _,      1,      _,      _,      _,      _,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1],
[1,     _,      _,      _,      _,      1,      _,      _,      _,      _,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1],
[1,     _,      _,      _,      _,      1,      _,      _,      _,      _,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      2,      1,      1],
[1,     1,      _,      1,      1,      1,      1,      1,      _,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      _,      _,      _,      1],
[1,     _,      _,      _,      _,      _,      _,      _,      _,      _,      1,      _,      _,      _,      _,      _,      _,      _,      _,      1,      _,      _,      _,      _,      _,      1],
[1,     _,      _,      _,      _,      _,      _,      _,      _,      _,      1,      _,      _,      _,      _,      _,      _,      _,      _,      _,      _,      _,      _,      _,      _,      2],
[1,     1,      1,      1,      1,      _,      1,      1,      1,      1,      1,      _,      _,      _,      _,      _,      _,      _,      _,      1,      _,      _,      _,      _,      _,      1],
[1,     _,      _,      1,      _,      _,      _,      _,      _,      _,      1,      1,      _,      1,      1,      1,      1,      1,      1,      1,      1,      1,      _,      _,      _,      1],
[1,     _,      _,      1,      _,      _,      _,      _,      _,      _,      1,      1,      _,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      2,      1,      1],
[1,     _,      _,      _,      _,      _,      _,      _,      _,      _,      _,      _,      _,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1],
[1,     _,      _,      1,      _,      _,      _,      _,      _,      _,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1],
[1,     1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1]
        ]
        self.carte_dict = {}
        self.get_map()

    def get_map(self):
        for y, ligne in enumerate(self.carte):
            for x, valeur in enumerate(ligne):
                if valeur:
                    self.carte_dict[(x, y)] = valeur  # permet de cataloguer les positions de toutes les paroies
        print(self.carte_dict)

    def draw(self):
        [pygame.draw.rect(self.jeu.fenetre, 'darkgray', ((pos[0] * 100)/5, (pos[1] * 100)/5, 20, 20), 2)
         for pos in self.carte_dict]

import pygame

import colors
import functions


class orb(pygame.sprite.Sprite):
    """
    [summary]
    """

    MIN_MASS = 2
    MAX_MASS = 10

    MIN_RADIUS = 2
    MAX_RADIUS = 5

    def __init__(self, x, y, mass, color):
        """
        [summary]
        
        Arguments:
            x {[type]} -- [description]
            y {[type]} -- [description]
            mass {[type]} -- [description]
            color {[type]} -- [description]
        """

        super(orb, self).__init__()

        self.mass = mass
        self.radius = int(functions.map_range(
            mass, (orb.MIN_MASS, orb.MAX_MASS), (orb.MIN_RADIUS, orb.MAX_RADIUS)))

        diameter = 2 * self.radius
        self.rect = pygame.Rect(0, 0, diameter, diameter)
        self.rect.center = (x, y)

        self.color = color

import pygame

import colors
import functions
import numpy as np


class orb(pygame.sprite.Sprite):
    """
    [summary]
    """

    MIN_MASS = 10
    MAX_MASS = 100

    MIN_RADIUS = 2
    MAX_RADIUS = 12

    ORB_COLORS = [
        colors.RED,
        colors.PURPLE,
        colors.ORANGE,
        colors.PINK_SLIME,
        colors.LIGHT_ARMY_GREEN
    ]

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
    
    def get_location(self):
        return self.rect.center
    
    def render(self, surface, scale=1, xoff=0, yoff=0):
        location_vector = np.array(self.get_location())
        scale_vector = np.array([[scale, 0], [0, scale]])

        scaled_vector = location_vector.dot(scale_vector)
        x, y = scaled_vector

        offsetted_x = int(x + xoff)
        offsetted_y = int(y + yoff)
        pos = (offsetted_x, offsetted_y)

        radius = int(self.radius * scale)

        pygame.draw.circle(surface, self.color, pos, radius)

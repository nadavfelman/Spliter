from random import choice, randint

import numpy as np
import pygame

import colors
import settings


class food(pygame.sprite.Sprite):
    """[summary]

    """
    MIN_VALUE = 3
    MAX_VALUE = 10

    POSSIBLE_COLORS = [colors.RED,
                       colors.PURPLE,
                       colors.ORANGE,
                       colors.PINK_SLIME,
                       colors.LIGHT_ARMY_GREEN]

    def __init__(self, location, value, color):
        self.location = location
        self.value = value
        self.color = color
        self.radius = int(value / 2.5)  # radius of the circle, it has connection to the value
        self.width = 1

    def draw(self, surface, scale=1, xoff=0, yoff=0):
        vector = np.array([self.location.x, self.location.y])
        scale_vector = np.array([[scale, 0], [0, scale]])

        scaled_vector = vector.dot(scale_vector)
        x, y = scaled_vector

        offseted_x = x + xoff
        offseted_y = y + yoff
        pos = (int(offseted_x), int(offseted_y))

        radius = int(self.radius * scale)

        pygame.draw.circle(surface, self.color, pos, radius)

    @staticmethod
    def new_random():
        # get new random location
        x = randint(0, settings.WINDOW_WIDTH)
        y = randint(0, settings.WINDOW_HEIGHT)
        location = pygame.math.Vector2(x, y)

        # get random value
        value = randint(food.MIN_VALUE, food.MAX_VALUE)

        # choose random color
        color = choice(food.POSSIBLE_COLORS)

        # return new object
        return food(location, value, color)

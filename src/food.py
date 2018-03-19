from random import randint, choice

import pygame

import colors
import settings


class food(pygame.sprite.Sprite):
    """[summary]

    """
    MIN_VALUE = 1
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
        self.radius = value  # radius of the circle, it has connection to the value
        self.width = 1

    def draw(self, surface, scale=1, xoff=0, yoff=0):
        offseted_x = self.location.x + xoff * scale
        offseted_y = self.location.y + yoff * scale
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

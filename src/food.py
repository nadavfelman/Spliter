from random import randint, choice

import pygame

import colors
import global_variables


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

    def draw(self, surface):
        location = (int(self.location.x), int(self.location.y))
        pygame.draw.circle(surface, self.color, location, self.radius, 1)

    @staticmethod
    def new_random():
        # get new random location
        x = randint(0, global_variables.WINDOW_WIDTH)
        y = randint(0, global_variables.WINDOW_HEIGHT)
        location = pygame.math.Vector2(x, y)

        # get random value
        value = randint(food.MIN_VALUE, food.MAX_VALUE)

        # choose random color
        color = choice(food.POSSIBLE_COLORS)

        # return new object
        return food(location, value, color)

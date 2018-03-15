import pygame
import colors
from random import randint

class food(pygame.sprite.Sprite):
    """[summary]
    
    """
    def __init__(self, location, color, radius, width):
        self.location = location
        self.color = color
        self.radius = radius
        self.width = width
    
    def draw(self, surface):
        rect = pygame.draw.circle(surface, self.color, (int(self.location.x), int(self.location.y)), self.radius, 1)


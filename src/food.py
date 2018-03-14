import pygame
import colors
from random import randint

class food(pygame.sprite.Sprite):
    """[summary]
    
    """
    def __init__(self, location=None, color=None, radius=None, width=None):
        self.location = location or pygame.math.Vector2(int(randint(0,960)), int(randint(0,540)))
        self.color = color or colors.WHITE
        self.radius = radius or 5
        self.width = width or 2
    
    def draw(self, surface):
        rect = pygame.draw.circle(surface, self.color, (int(self.location.x), int(self.location.y)), self.radius, 1)
        surface.fill(self.color, rect)


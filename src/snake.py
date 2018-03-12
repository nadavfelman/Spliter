import math
import pygame


class joint(object):
    """
    [summary]  
    """

    def __init__(self, location, length, angle=0, son=None, color=(255, 255, 255)):
        """[summary]

        Arguments:
            location {pygame.math.Vector2} -- location vector of the joint base
            length {int} -- length of the joint

        Keyword Arguments:
            angle {int} -- angle of the joint, relative to the prevues joint (default: {0})
            son {joint} -- the next joint (the joint connected to this one) (default: {None})
        """
        self.location = location
        self.length = length
        self.angle = angle
        self.son = son
        self.color = color

    def move(self, new_location, max_pixels=None):
        """[summary]

        Arguments:
            new_location {pygame.math.Vector2} -- [description]

        Keyword Arguments:
            max_pixels {int} -- [description] (default: {None})
        """
        dx = new_location.x - self.location.x
        dy = new_location.y - self.location.y
        self.angle = math.atan2(dy, dx)

        if self.head() != new_location:
            if self.location.distance_to(new_location) - self.length > self.length:
                new_x = self.location.x + max_pixels * math.cos(self.angle)
                new_y = self.location.y + max_pixels * math.sin(self.angle)
                self.location = pygame.math.Vector2(new_x, new_y)
            else:
                new_x = new_location.x - self.length * math.cos(self.angle)
                new_y = new_location.y - self.length * math.sin(self.angle)
                self.location = pygame.math.Vector2(new_x, new_y)

        if self.son:
            self.son.move(self.location, max_pixels)

    def head(self):
        """[summary]

        Returns:
            [type] -- [description]
        """

        head_x = self.location.x + self.length * math.cos(self.angle)
        head_y = self.location.y + self.length * math.sin(self.angle)
        return pygame.math.Vector2(head_x, head_y)

    def draw(self, screen):
        """[summary]

        Arguments:
            screen {[type]} -- [description]
        """

        pygame.draw.line(screen, self.color, self.location, self.head(), 5)
        if self.son:
            self.son.draw(screen)


class snake(pygame.sprite.Sprite):
    """
    [summary]
    """

    def __init__(self, location, length=1):
        self.joints = joint(location, 1)

    def add_joints(self, amount):
        pos = self.joints
        while pos.son != None:
            pos = pos.son
        for _ in xrange(amount):
            pos.son = joint(pygame.math.Vector2(0, 0), 1)
            pos = pos.son

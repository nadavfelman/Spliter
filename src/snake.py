import math
import pygame


class joint(object):
    """
    [summary]  
    """

    def __init__(self, location, length, angle=0, color=(255, 255, 255), width=5):
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
        self.color = color
        self.width = width

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
            if max_pixels and self.location.distance_to(new_location) - self.length > max_pixels:
                new_x = self.location.x + max_pixels * math.cos(self.angle)
                new_y = self.location.y + max_pixels * math.sin(self.angle)
                self.location = pygame.math.Vector2(new_x, new_y)
            else:
                new_x = new_location.x - self.length * math.cos(self.angle)
                new_y = new_location.y - self.length * math.sin(self.angle)
                self.location = pygame.math.Vector2(new_x, new_y)

    def head(self):
        """[summary]

        Returns:
            [type] -- [description]
        """

        head_x = self.location.x + self.length * math.cos(self.angle)
        head_y = self.location.y + self.length * math.sin(self.angle)
        return pygame.math.Vector2(head_x, head_y)

    def draw(self, surface, color=None, width=None):
        """[summary]

        Arguments:
            surface {[type]} -- [description]
        """
        color = color or self.color
        width = width or self.width
        pygame.draw.line(surface, self.color, self.location, self.head(), width)


class snake(pygame.sprite.Sprite):
    """
    [summary]
    """

    def __init__(self, location):
        self.head = joint(location, 10, color=(255, 0, 0))
        self.tail = []

    def length(self):
        return 1 + len(self.tail)

    def move(self, new_location, max_pixels=None):
        self.head.move(new_location, max_pixels)
        pre = self.head.location
        for j in self.tail:
            j.move(pre)
            pre = j.location

    def draw(self, surface):
        self.head.draw(surface)
        for j in self.tail:
            j.draw(surface)

    def add(self, amount):
        for _ in xrange(amount):
            if self.tail:
                loc = self.tail[-1].location
            else:
                loc = self.head.location
            self.tail.append(joint(loc, 5))

    def sub(self, amount):
        self.tail = self.tail[0:-amount]

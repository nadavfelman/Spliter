import math
import pygame


class joint(object):
    """
    [summary]  
    """

    def __init__(self, location, length, **kwargs):
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
        self.angle = kwargs.get('angle', 0) 
        self.color = kwargs.get('color', (255, 255, 255))
        self.width = kwargs.get('width', 5)

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

    def draw(self, surface, **kwargs):
        """[summary]

        Arguments:
            surface {[type]} -- [description]
        """
        color = kwargs.get('color', self.color)
        width = kwargs.get('width', self.width)
        pygame.draw.line(surface, color, self.location, self.head(), width)


class snake(pygame.sprite.Sprite):
    """
    [summary]
    """

    def __init__(self, location, **kwargs):
        """[summary]
        
        Arguments:
            location {[type]} -- [description]
        """

        self.name = ''
        self.mess = 0

        self.default_speed = kwargs.get('default_speed', 10)
        self.high_speed = kwargs.get('high_speed', 20)

        self.head_color = kwargs.get('head_color', (255,0,0))
        self.head_width = kwargs.get('head_width', 2)
        self.head_length = kwargs.get('head_length', 10)

        self.tail_color = kwargs.get('tail_color', (255,255,255))
        self.tail_width = kwargs.get('tail_width', 1)
        self.tail_length = kwargs.get('tail_length', 4)
        
        self.head = joint(location, 10, color=self.head_color, width=self.head_width)
        self.tail = []
        self.speed = self.default_speed

    def length(self):
        """[summary]
        
        Returns:
            [type] -- [description]
        """

        return 1 + len(self.tail)

    def move(self, new_location, **kwargs):
        """[summary]
        
        Arguments:
            new_location {[type]} -- [description]
        """

        speed = kwargs.get('speed', self.speed)

        self.head.move(new_location, speed)
        pre = self.head.location
        for j in self.tail:
            j.move(pre)
            pre = j.location

    def draw(self, surface):
        """[summary]
        
        Arguments:
            surface {[type]} -- [description]
        """

        self.head.draw(surface)
        for j in self.tail:
            j.draw(surface)

    def add(self, amount, **kwargs):
        """[summary]
        
        Arguments:
            amount {[type]} -- [description]
        """

        color = kwargs.get('color', self.tail_color)
        width = kwargs.get('width', self.tail_width)
        length = kwargs.get('length', self.tail_length)

        for _ in xrange(amount):
            if self.tail:
                loc = self.tail[-1].location
            else:
                loc = self.head.location
            self.tail.append(joint(loc, length, color=color, width=width))

    def sub(self, amount):
        """[summary]
        
        Arguments:
            amount {[type]} -- [description]
        """

        self.tail = self.tail[0:-amount]

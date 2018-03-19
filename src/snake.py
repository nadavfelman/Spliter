import math

import pygame

import settings
import numpy as np


class joint(object):
    """
    [summary]
    """

    def __init__(self, location, distance, angle=0):
        """[summary]

        Arguments:
            location {pygame.math.Vector2} -- location vector of the joint base
            distance {int} -- distance from previous joint

        Keyword Arguments:
            angle {int} -- angle of the joint, relative to the prevues joint (default: {0})
            son {joint} -- the next joint (the joint connected to this one) (default: {None})
        """
        self.location = location
        self.distance = distance
        self.angle = angle

    def direct_to(self, location):
        """[summary]

        Arguments:
            location {[type]} -- [description]
        """

        dx = location.x - self.location.x
        dy = location.y - self.location.y
        self.angle = math.atan2(dy, dx)

    def move(self, new_location, speed=None):
        """[summary]

        Arguments:
            new_location {pygame.math.Vector2} -- [description]

        Keyword Arguments:
            speed {int} -- [description] (default: {None})
        """
        # chage the angle so it will point at the new location
        self.direct_to(new_location)

        # check if the joint needs to be moved
        # if the head of the joint is on the location it does not need to be moved
        if self.previous() != new_location:
            # check if any max pixels moving distance was given.
            # if was given it checks whether the distance need to be moved is greater than the max moving distance.
            # if this returns true constrain the movement to the max moving distance else move regularly.
            # see attache number 0000.
            if speed and self.location.distance_to(new_location) - self.distance > speed:
                new_x = self.location.x + speed * math.cos(self.angle)
                new_y = self.location.y + speed * math.sin(self.angle)
                self.location = pygame.math.Vector2(new_x, new_y)

            else:
                new_x = new_location.x - self.distance * math.cos(self.angle)
                new_y = new_location.y - self.distance * math.sin(self.angle)
                self.location = pygame.math.Vector2(new_x, new_y)

    def update(self, speed):
        """[summary]

        Arguments:
            speed {[type]} -- [description]
        """

        new_x = self.location.x + speed * math.cos(self.angle)
        new_y = self.location.y + speed * math.sin(self.angle)
        self.location = pygame.math.Vector2(new_x, new_y)

    def previous(self):
        """[summary]

        Returns:
            [type] -- [description]
        """

        head_x = self.location.x + self.distance * math.cos(self.angle)
        head_y = self.location.y + self.distance * math.sin(self.angle)
        return pygame.math.Vector2(head_x, head_y)


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
        self.length = 5

        self.default_speed = kwargs.get('default_speed', 1)
        self.high_speed = kwargs.get('high_speed', 7)

        self.head_color = kwargs.get('head_color', (255, 0, 0))
        self.head_radius = kwargs.get('head_radius', 5)
        self.head_length = kwargs.get('head_length', 3)

        self.tail_color = kwargs.get('tail_color', (255, 255, 255))
        self.tail_radius = kwargs.get('tail_radius', 5)
        self.tail_length = kwargs.get('tail_length', 3)

        self.head = joint(location, self.head_length)
        self.tail = []
        self.speed = self.default_speed

        self.increase_length(self.length)

    def size(self):
        return 0.02 * self.length + 1

    def move(self, **kwargs):
        """[summary]

        Arguments:
            new_location {[type]} -- [description]
        """

        speed = kwargs.get('speed', self.speed)

        self.head.update(speed)
        pre = self.head.location
        for sector in self.tail:
            sector.move(pre)
            pre = sector.location

    def update(self):
        self.move()

    def draw(self, surface, scale=1, xoff=0, yoff=0):
        """[summary]

        Arguments:
            surface {[type]} -- [description]
        """
        # matrix = np.array([[j.location.x, j.location.y] for j in self.tail])
        matrix = np.array([[j.location.x + xoff, j.location.y + yoff] for j in self.tail])
        scale_vector = np.array([[scale, 0], [0, scale]])
        # print matrix, scale_vector
        scaled_matrix = np.matmul(matrix, scale_vector)
        # print scaled_matrix
        # print np.array([[x +xoff*scale,y + yoff*scale] for x,y in scaled_matrix])
        # matrix2 = np.array([[j.location.x + xoff, j.location.y + yoff] for j in self.tail])
        # scaled_matrix2 = np.matmul(matrix2, scale_vector)
        # print scaled_matrix2
        # print()

        for x, y in scaled_matrix:
            # offseted_x = x + xoff * scale
            # offseted_y = y + yoff * scale
            pos = (int(x), int(y))

            radius = int(self.tail_radius * scale)

            pygame.draw.circle(surface, self.tail_color, pos, radius)

    def direct_to(self, location):
        dx = location.x - self.head.location.x
        dy = location.y - self.head.location.y
        self.head.angle = math.atan2(dy, dx)

    def set_angle(self, angle):
        self.head.angle = angle

    def increase_length(self, amount):
        """
        [summary]

        Arguments:
            amount {[type]} -- [description]
        """

        for _ in xrange(amount):
            if self.tail:
                loc = self.tail[-1].location
            else:
                loc = self.head.location
            self.tail.append(joint(loc, self.tail_length))

    def decrease_length(self, amount):
        """[summary]

        Arguments:
            amount {[type]} -- [description]
        """

        self.tail = self.tail[0: -amount]

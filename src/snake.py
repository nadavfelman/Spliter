import math

import numpy as np
import pygame

import settings
import colors


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
        # breke out if already in place
        if self.previous() == new_location:
            return
        
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
    DEFUALT_LENGTH = 10
    DEFAULT_REGULAR_SPEED = 1
    DEFAULT_HIGH_SPEED = 5
    DEFAULT_HEAD_COLOR = colors.RED
    DEFAULT_TAIL_COLOR = colors.GRAY66

    SHADOW_XOFF = 1
    SHADOW_YOFF = 1
    SHADOW_HEAD_COLOR = colors.DARK_RED
    SHADOW_TAIL_COLOR = colors.GRAY126

    def __init__(self, location, **kwargs):
        """[summary]

        Arguments:
            location {[type]} -- [description]
        """

        self.name = ''
        self.length = snake.DEFUALT_LENGTH

        self.regular_speed = kwargs.get(
            'default_speed', snake.DEFAULT_REGULAR_SPEED)
        self.high_speed = kwargs.get('high_speed', snake.DEFAULT_HIGH_SPEED)

        self.head_color = kwargs.get('head_color', snake.DEFAULT_HEAD_COLOR)
        self.tail_color = kwargs.get('tail_color', snake.DEFAULT_TAIL_COLOR)

        self.head = joint(location, self.distance)
        self.tail = []
        self.speed = self.regular_speed

        self.increase_length(self.length)

    def radius(self):
        return 0.05 * self.length + 2

    def distance(self):
        return self.radius() / 2

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
        if self.head.distance != self.distance():
            self.change_distance(self.distance())
        self.move()

    def draw(self, surface, scale=1, xoff=0, yoff=0):
        """[summary]
        
        Arguments:
            surface {[type]} -- [description]
        
        Keyword Arguments:
            scale {int} -- [description] (default: {1})
            xoff {int} -- [description] (default: {0})
            yoff {int} -- [description] (default: {0})
        """

        # scale vector (for matrix or vector multiplication)
        scale_vector = np.array([[scale, 0], [0, scale]])
        # scaled radius of the circle
        radius = int(self.radius() * scale)

        # draw trail
        # matrix of all the point in the trail
        matrix = np.array([[j.location.x, j.location.y] for j in self.tail[::-1]])
        # scaled matrix of the trail
        scaled_matrix = np.matmul(matrix, scale_vector)

        for x, y in scaled_matrix:
            # scaled x and y of one point with the offset applied
            pos = (int(x + xoff), int(y + yoff))  # position of the joint
            shadow_pos = (int(x + xoff + snake.SHADOW_XOFF), int(y + yoff + snake.SHADOW_YOFF))  # position of the shadow

            # draw the shadow of the joint
            pygame.draw.circle(surface, snake.SHADOW_TAIL_COLOR, shadow_pos, radius)
            pygame.draw.circle(surface, self.tail_color, pos, radius)  # draw the joint

        # draw head
        # vector representing the location of head
        vector = np.array([self.head.location.x, self.head.location.y])
        scaled_vector = vector.dot(scale_vector)  # scaled vector of head
        x, y = scaled_vector  # scaled x and y

        # scaled x and y with the offset applied
        pos = (int(x + xoff), int(y + yoff))  # position of the joint
        shadow_pos = (int(x + xoff + snake.SHADOW_XOFF), int(y + yoff + snake.SHADOW_YOFF))  # position of the shadow

        # draw the shadow of the joint
        pygame.draw.circle(surface, snake.SHADOW_HEAD_COLOR, shadow_pos, radius)
        pygame.draw.circle(surface, self.head_color, pos, radius)  # draw the joint

    def direct_to(self, location):
        dx = location.x - self.head.location.x
        dy = location.y - self.head.location.y
        self.head.angle = math.atan2(dy, dx)

    def set_angle(self, angle, lim=None):
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
            self.tail.append(joint(loc, self.distance()))

    def decrease_length(self, amount):
        """[summary]

        Arguments:
            amount {[type]} -- [description]
        """

        self.tail = self.tail[0: -amount]

    def change_distance(self, distance):
        self.head.distance = distance
        for j in self.tail:
            j.distance = distance

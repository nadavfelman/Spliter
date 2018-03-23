import math
import pygame
import colors
import numpy as np
import render


class section(pygame.sprtie.Sprtie):
    """
    [summary] 

    """

    def __init__(self, location, distance, radius, angle=0):
        super(section, self).__init__()

        diameter = 2 * radius
        self.rect = pygame.Rect(0, 0, diameter, diameter)
        self.rect.center = location
        self.distance = distance
        self.radius = radius
        self.angle = angle

    def get_location(self):
        return self.rect.center

    def set_location(self, location):
        self.rect.center = location

    def set_radius(self, radius):
        diameter = 2 * self.radius
        center = self.rect.center
        self.rect.width = diameter
        self.rect.height = diameter
        self.rect.center = center

    def direct_to(self, location):
        self_x, self_y = self.get_location()
        x, y = location

        dx = x - self_x
        dy = y - self_y
        self.angle = math.atan2(dy, dx)

    def next_location(self):
        self_x, self_y = self.get_location()
        next_x = self_x + self.distance * math.cos(self.angle)
        next_y = self_y + self.distance * math.sin(self.angle)
        return pygame.math.Vector2(next_x, next_y)

    def relocate(self, location, max_move=None):
        # break out if already in place
        if self.next_location() == location:
            return

        # change the angle so it will point at the new location
        self.direct_to(location)

        # check if the joint needs to be moved
        # if the head of the joint is on the location it does not need to be moved
        if self.next_location() != location:
            # check if any max pixels moving distance was given.
            # if was given it checks whether the distance need to be moved is greater than the max moving distance.
            # if this returns true constrain the movement to the max moving distance else move regularly.
            # see attache number 0000.
            self_x, self_y = self.get_location()
            loc_x, loc_y = location

            distance_to = math.sqrt(
                (self_x - loc_x) ** 2 + (self_y - loc_y) ** 2)

            if max_move and distance_to - self.distance > max_move:
                new_x = self_x + max_move * math.cos(self.angle)
                new_y = self_y + max_move * math.sin(self.angle)
                self.set_location((new_x, new_y))

            else:
                new_x = loc_x - self.distance * math.cos(self.angle)
                new_y = loc_y - self.distance * math.sin(self.angle)
                self.set_location((new_x, new_y))


class snake(pygame.sprite.Sprite):
    """
    [summary]
    """
    DEFAULT_MASS = 10
    DEFAULT_HEAD_COLOR = colors.RED
    DEFAULT_TAIL_COLOR = colors.GRAY66

    # name variables
    NAME_FONT_SIZE = 17
    NAME_FONT_COLOR = colors.GRAY25

    # render variables
    SHADOW_XOFF = 1
    SHADOW_YOFF = 1
    SHADOW_HEAD_COLOR = colors.DARK_RED
    SHADOW_TAIL_COLOR = colors.GRAY126

    def __init__(self, location, name):
        self.name = name
        self.mass = snake.DEFAULT_MASS

        self.head_color = snake.DEFAULT_HEAD_COLOR
        self.tail_color = snake.DEFAULT_TAIL_COLOR

        self.head = section(location, self.get_distance(), self.get_radius())
        self.tail = []

    def get_radius(self):
        return self.mass / 1000 + 2

    def get_distance(self):
        return self.get_radius() / 2 + 1

    def get_length(self):
        return self.mass / 100 + 10

    def get_location(self):
        return self.head.get_location()

    def update_length(self):
        length = int(self.get_length())
        dl = len(self.tail) - length

        if dl < 0:
            for _ in xrange(abs(dl)):
                if self.tail:
                    loc = self.tail[-1].get_location()
                else:
                    loc = self.head.get_location()

                new_sector = section(loc, self.get_distance(), self.get_radius())
                self.tail.append(new_sector)
        elif dl > 0:
            self.tail = self.tail[0: -abs(dl)]

    def update_distance(self):
        new_distance = self.get_distance()
        self.head.distance = new_distance
        for j in self.tail:
            j.distance = new_distance

    def update_radius(self):
        new_radius = self.get_radius()
        self.head.distance = new_radius
        for j in self.tail:
            j.distance = new_radius

    def update_mass(self):
        self.update_length()
        self.update_distance()
        self.update_radius()

    def add_mass(self, amount):
        self.mass += amount
        self.update_mass()

    def sub_mass(self, amount):
        self.mass -= amount
        self.update_mass()

    def relocate(self, location):
        self.head.relocate(location)
        previous_location = self.head.get_location()
        for sector in self.tail:
            sector.relocate(previous_location)
            previous_location = sector.get_location()

    def render(self, surface, scale=1, xoff=0, yoff=0):
        self.render_snake(surface, scale=scale, xoff=xoff, yoff=yoff)
        self.render_name(surface, scale=scale, xoff=xoff, yoff=yoff)

    def render_snake(self, surface, scale=1, xoff=0, yoff=0):
        # scale vector (for matrix or vector multiplication)
        scale_vector = np.array([[scale, 0], [0, scale]])
        # scaled radius of the circle
        scaled_radius = int(self.radius() * scale)

        # draw trail
        # matrix of all the point in the trail
        matrix = np.array([sector.get_location()
                           for sector in self.tail[::-1]])
        # scaled matrix of the trail
        scaled_matrix = np.matmul(matrix, scale_vector)

        for x, y in scaled_matrix:
            # scaled x and y of one point with the offset applied
            x = int(x + xoff)
            y = int(y + yoff)
            pos = (x, y)  # position of the joint
            shadow_x = int(x + xoff + snake.SHADOW_XOFF)
            shadow_y = int(y + yoff + snake.SHADOW_YOFF)
            shadow_pos = (shadow_x, shadow_y)  # position of the shadow

            # draw the shadow of the joint
            pygame.draw.circle(
                surface, snake.SHADOW_TAIL_COLOR, shadow_pos, scaled_radius)
            pygame.draw.circle(surface, self.tail_color,
                               pos, scaled_radius)  # draw the joint

        # draw head
        # vector representing the location of head
        vector = np.array(self.head.get_location())
        scaled_vector = vector.dot(scale_vector)  # scaled vector of head
        x, y = scaled_vector  # scaled x and y

        # scaled x and y with the offset applied
        x = int(x + xoff)
        y = int(y + yoff)
        pos = (x, y)  # position of the joint
        shadow_x = int(x + xoff + snake.SHADOW_XOFF)
        shadow_y = int(y + yoff + snake.SHADOW_YOFF)
        shadow_pos = (shadow_x, shadow_y)  # position of the shadow

        # draw the shadow of the joint
        pygame.draw.circle(surface, snake.SHADOW_HEAD_COLOR,
                           shadow_pos, scaled_radius)
        pygame.draw.circle(surface, self.head_color,
                           pos, scaled_radius)  # draw the joint

    def render_name(self, surface, scale=1, xoff=0, yoff=0):
        x, y = self.get_location()
        x = x * scale + xoff
        name_offset = self.radius() + snake.DEFAULT_NAME_SIZE
        y = y * scale + yoff - name_offset

        size = snake.NAME_FONT_SIZE
        color = snake.NAME_FONT_COLOR
        
        render.message_display(surface, self.name, x, y, size, color)
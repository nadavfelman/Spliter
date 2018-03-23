"""
TODO:
    - complete filter in camera in render function.
    - complete snake_render
    - complete orb_render
"""

import pygame

import colors
import dataSets


class render(object):
    """
    [summary]  
    """

    DEFAULT_ZOOM = 1

    def __init__(self, display_rect, board_rect, dataBase):
        """[summary]

        Arguments:
            display_rect {[type]} -- [description]
            dataBase {dataSets.dataBase} -- [description]
        """
        self.display_rect = display_rect.copy()
        self.camera_rect = display_rect.copy()
        self.background_ = background(board_rect)
        self.dataBase = dataBase
        self.zoom = render.DEFAULT_ZOOM

    def set_camera_pos(self, x, y):
        self.camera_rect.center = (x, y)

    def set_camera_dimensions(self, width, height):
        self.camera_rect.width = width
        self.camera_rect.height = height

    def set_zoom(self, zoom):
        """

        zoom < 1 : zooming out, making everything smaller, more surface view.
        zoom > 1 : zooming in, making everything lager, less surface view.

        Arguments:
            scale {[type]} -- [description]
        """
        self.zoom = zoom

        center = self.camera_rect.center
        self.camera_rect.width = self.display_rect.width * (1 / zoom)
        self.camera_rect.height = self.display_rect.height * (1 / zoom)
        self.camera_rect.center = center

    def render(self, surface):
        scale = self.zoom
        xoff = self.camera_rect.left
        yoff = self.camera_rect.top

        snakes = self.dataBase.iter_snakes_objects()
        in_camera_snakes = filter(
            lambda s: pygame.sprite.collide_rect(self.camera_rect, s), snakes)
        for s in in_camera_snakes:
            render_snake(surface, s, scale, xoff, yoff)

        orbs = self.dataBase.iter_snakes_objects()
        in_camera_orbs = filter(
            lambda o: pygame.sprite.collide_rect(self.camera_rect, o), orbs)
        for o in in_camera_orbs:
            render_orb(surface, o, scale, xoff, yoff)


def render_snake(surface, obj, scale=1, xoff=0, yoff=0):
    obj.render(surface, scale=scale, xoff=xoff, yoff=yoff)


def render_orb(surface, obj, scale=1, xoff=0, yoff=0):
    obj.render(surface, scale=scale, xoff=xoff, yoff=yoff)


def message_display(surface, text, x, y, size, color):
    font = pygame.font.Font('freesansbold.ttf', size)
    textSurface = font.render(text, True, color)
    TextRect = textSurface.get_rect()
    TextRect.center = (x, y)
    surface.blit(textSurface, TextRect)


class background(object):
    X_SPACING = 100
    Y_SPACING = 100
    LINE_THICKNESS = 1

    BACKGROUND_COLOR = colors.WARM_WHITE
    SECONDARY_COLOR = colors.GRAY126
    OUTZONE_COLOR = colors.LIGHT_PINK

    def __init__(self, rect, line_thickness=None, x_spacing=None, y_spacing=None):
        self.board_rect = rect  # board rect

        self.line_thickness = line_thickness or background.LINE_THICKNESS
        self.x_spacing = x_spacing or background.X_SPACING
        self.y_spacing = y_spacing or background.Y_SPACING

    def draw(self, surface, camera_rect, scl):
        camera_x, camera_y = camera_rect.center
        camera_x, camera_y = camera_x * scl, camera_y * scl

        width, height = camera_rect.width, camera_rect.height
        top = int(camera_y - height / 2)
        right = int(camera_x - width / 2)
        buttom = int(camera_y + height / 2)
        left = int(camera_x + width / 2)

        surface.fill(background.BACKGROUND_COLOR)
        for x in filter(lambda x: x % int((self.line_thickness + self.x_spacing) * scl) == 0, xrange(right, left + 1)):
            pygame.draw.line(surface, background.SECONDARY_COLOR,
                             (x - right, 0), (x - right, height), self.line_thickness)

        for y in filter(lambda y: y % int((self.line_thickness + self.y_spacing) * scl) == 0, xrange(top, buttom + 1)):
            pygame.draw.line(surface, background.SECONDARY_COLOR,
                             (0, y - top), (width, y - top), self.line_thickness)

        for x in filter(lambda x: x < self.board_rect.left or x > self.board_rect.right, xrange(right, left + 1)):
            pygame.draw.line(surface, background.OUTZONE_COLOR,
                             (x - right, 0), (x - right, height), 1)

        for y in filter(lambda y: y < self.board_rect.top or y > self.board_rect.bottom, xrange(top, buttom + 1)):
            pygame.draw.line(surface, background.OUTZONE_COLOR,
                             (0, y - top), (width, y - top), 1)

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

    def __init__(self, display_rect, dataBase):
        """[summary]

        Arguments:
            display_rect {[type]} -- [description]
            dataBase {dataSets.dataBase} -- [description]
        """
        self.display = display_rect.copy()
        self.camera = display_rect.copy()
        self.dataBase = dataBase
        self.zoom = 1

    def set_camera_pos(self, x, y):
        self.camera.center = (x, y)

    def set_camera_dimensions(self, width, height):
        self.camera.width = width
        self.camera.height = height

    def set_zoom(self, zoom):
        """

        zoom < 1 : zooming out, making everything smaller, more surface view.
        zoom > 1 : zooming in, making everything lager, less surface view.

        Arguments:
            scale {[type]} -- [description]
        """
        self.zoom = zoom

        center = self.camera.center
        self.camera.width = self.display.width * (1 / zoom)
        self.camera.height = self.display.height * (1 / zoom)
        self.camera.center = center

    def render(self, surface):
        scale = self.zoom
        xoff = self.camera.left
        yoff = self.camera.top

        snakes = self.dataBase.iter_snakes_objects()
        in_camera_snakes = snakes  # filter()
        for s in in_camera_snakes:
            render_snake(surface, s, scale, xoff, yoff)

        orbs = self.dataBase.iter_snakes_objects()
        in_camera_orbs = orbs  # filter()
        for o in in_camera_orbs:
            render_orb(surface, o, scale, xoff, yoff)


def render_snake(surface, obj, scl=1, xoff=0, yoff=0):
    pass


def render_orb(surface, obj, scl=1, xoff=0, yoff=0):
    pass


def message_display(surface, text, x, y, size, color):
    font = pygame.font.Font('freesansbold.ttf', size)
    textSurface = font.render(text, True, color)
    TextRect = textSurface.get_rect()
    TextRect.center = (x, y)
    surface.blit(textSurface, TextRect)

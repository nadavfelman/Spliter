import colors
import pygame


class background(object):
    X_SPACING = 100
    Y_SPACING = 100
    LINE_THICKNESS = 1

    BACKGROUND_COLOR = colors.WARM_WHITE
    SECONDARY_COLOR = colors.GRAY126
    OUTZONE_COLOR = colors.LIGHT_PINK

    def __init__(self, min_x, max_x, min_y, max_y, width, height, line_thickness=None, x_spacing=None, y_spacing=None):
        self.width = width
        self.height = height

        self.mix_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y

        self.line_thickness = line_thickness or background.LINE_THICKNESS
        self.x_spacing = x_spacing or background.X_SPACING
        self.y_spacing = y_spacing or background.Y_SPACING

    def draw(self, surface, camera_x, camera_y, scl):
        camera_x , camera_y = camera_x * scl, camera_y * scl
        width, height = self.width, self.height
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

        for x in filter(lambda x: x < self.mix_x or x > self.max_x, xrange(right, left + 1)):
            pygame.draw.line(surface, background.OUTZONE_COLOR,
                             (x - right, 0), (x - right, height), 1)

        for y in filter(lambda y: y < self.min_y or y > self.max_y, xrange(top, buttom + 1)):
            pygame.draw.line(surface, background.OUTZONE_COLOR,
                             (0, y - top), (width, y - top), 1)

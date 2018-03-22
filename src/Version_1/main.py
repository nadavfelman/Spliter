import math

import pygame

import colors
import food
import functions
import settings
import snake
import render

exit_ = False
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode(
    (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT), pygame.RESIZABLE)

s = snake.snake(pygame.math.Vector2(0, 0), default_speed=0.7)
b = render.background(0, settings.BOARD_WIDTH, 0, settings.BOARD_HEIGHT, settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)

foods = []
for _ in xrange(100):
    foods.append(food.food.new_random())

while not exit_:
    print 'fps: {}'.format(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_ = True
    
    cx = s.head.location.x
    cy = s.head.location.y
    scl = 15 / s.radius()

    b.draw(screen, cx, cy, scl)
    # screen.fill(settings.BACKGROUND_COLOR)

    xoff = -s.head.location.x * scl + settings.WINDOW_WIDTH / 2
    yoff = -s.head.location.y * scl + settings.WINDOW_HEIGHT / 2

    for f in foods:
        f.draw(screen, scale=scl, xoff=xoff, yoff=yoff)

    mouse_loc = pygame.mouse.get_pos()
    middle_loc = (settings.WINDOW_WIDTH / 2,
                  settings.WINDOW_HEIGHT / 2)
    s.set_angle(functions.incline_angle(middle_loc, mouse_loc), lim=math.radians(1.5))
    s.move()
    s.draw(screen, scl, xoff, yoff)

    pygame.draw.rect(screen, (0,0,0), (xoff - 5, yoff - 5, 10, 10))

    pygame.display.flip()
    clock.tick(settings.REFRESH_RATE)

import math

import pygame

import colors
import food
import settings
import snake
import functions

exit_ = False
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode(
    (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))

s = snake.snake(pygame.math.Vector2(0, 0), default_speed=1)

foods = []
for _ in xrange(30):
    foods.append(food.food.new_random())

while not exit_:
    print 'fps: {}'.format(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_ = True

    screen.fill(settings.DEADZONE_COLOR)
    game_board = pygame.Surface(
        (settings.BOARD_WIDTH, settings.BOARD_HEIGHT))
    screen.fill(settings.BACKGROUND_COLOR)

    scl = 2 # 6 / s.size()
    xoff = -s.head.location.x + settings.WINDOW_WIDTH / 2
    yoff = -s.head.location.y + settings.WINDOW_HEIGHT / 2

    mouse_loc = pygame.mouse.get_pos()
    middle_loc = (settings.WINDOW_WIDTH / 2,
                  settings.WINDOW_HEIGHT / 2)
    s.set_angle(functions.incline_angle(middle_loc, mouse_loc))
    s.move()
    s.draw(game_board, scl, xoff, yoff)

    for f in foods:
        f.draw(game_board, scl, xoff, yoff)

    screen.blit(game_board, (0, 0))

    pygame.display.flip()
    clock.tick(60)

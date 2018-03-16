import math

import pygame

import colors
import food
import global_variables
import snake
import functions

exit_ = False
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode(
    (global_variables.WINDOW_WIDTH, global_variables.WINDOW_HEIGHT))

s = snake.snake(pygame.math.Vector2(0, 0), default_speed=1)
s.add(100)

foods = []
for _ in xrange(30):
    foods.append(food.food.new_random())

while not exit_:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_ = True

    screen.fill(colors.DARK_DEAD_RED)
    game_board = pygame.Surface(
        (global_variables.BOARD_WIDTH, global_variables.BOARD_HEIGHT))

    mouse_loc = pygame.mouse.get_pos()
    middle_loc = (global_variables.WINDOW_WIDTH / 2,
                  global_variables.WINDOW_HEIGHT / 2)
    s.set_angle(functions.incline_angle(middle_loc, mouse_loc))
    s.update()
    s.draw(game_board)

    for f in foods:
        f.draw(game_board)

    scl = 6 / s.head.width

    x = -s.head.location.x * scl + global_variables.WINDOW_WIDTH / 2
    y = -s.head.location.y * scl + global_variables.WINDOW_HEIGHT / 2

    scaled_width = global_variables.BOARD_WIDTH * scl
    scaled_height = global_variables.BOARD_HEIGHT * scl
    scaled = pygame.transform.scale(game_board, (scaled_width, scaled_height))
    screen.blit(scaled, (x, y))

    pygame.display.flip()
    clock.tick(60)

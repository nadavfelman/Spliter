import math

import pygame

import colors
import food
import global_variables
import snake

exit_ = False
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode(
    (global_variables.WINDOW_WIDTH, global_variables.WINDOW_HEIGHT))

s = snake.snake(pygame.math.Vector2(0, 0))
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

    s.update(pygame.math.Vector2(*pygame.mouse.get_pos()), speed=5)
    s.draw(game_board)

    for f in foods:
        f.draw(game_board)

    x = -s.head.location.x + global_variables.WINDOW_WIDTH / 2
    y = -s.head.location.y + global_variables.WINDOW_HEIGHT / 2
    screen.blit(game_board, (x, y))
    print x, y

    pygame.display.flip()
    clock.tick(60)

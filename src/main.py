import snake
import pygame
import math
import food

exit_ = False
clock = pygame.time.Clock()


pygame.init()
screen = pygame.display.set_mode((960, 540))

s = snake.snake(pygame.math.Vector2(0,0))
s.add(300)

foods = []
for _ in xrange(50):
    foods.append(food.food())

while not exit_:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_ = True

    s.move(pygame.math.Vector2(*pygame.mouse.get_pos()), 20)
    s.draw(screen)

    for f in foods:
        f.draw(screen)

    pygame.display.flip()
    clock.tick(30)

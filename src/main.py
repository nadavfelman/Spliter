import snake
import pygame
import math

exit_ = False
clock = pygame.time.Clock()


pygame.init()
screen = pygame.display.set_mode((960, 540))

s = snake.joint(pygame.math.Vector2(5,10), 40, son=snake.joint(pygame.math.Vector2(5,5), 20, son=snake.joint(pygame.math.Vector2(5,5), 70, color=(0,255,0)), color=(255,0,0)))

while not exit_:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_ = True

    s.move(pygame.math.Vector2(*pygame.mouse.get_pos()), 20)
    s.draw(screen)

    # print s.location, s.head(), math.degrees(s.angle)

    pygame.display.flip()
    clock.tick(60)

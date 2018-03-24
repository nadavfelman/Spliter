import pygame
import dataSets
import render
import snake
import playerSnake
import orb
import functions
import math
import random
import settings


def main():
    pygame.init()
    display = pygame.display.set_mode(settings.WINDOW_SIZE, pygame.FULLSCREEN)
    board = pygame.Rect(0, 0, 9600, 5400)
    CLOCK = pygame.time.Clock()
    dataBase = dataSets.dataBase()
    rendering = render.render(display.get_rect(), board, dataBase)

    player = playerSnake.playerSnake((0, 0), 'nadav')
    dataBase.add_snake('1', player)
    rendering.set_player(player)

    for i in xrange(100):
        dataBase.add_orb(i, orb.orb(random.randint(0, 200), random.randint(0, 200), random.randint(2, 20), random.choice(orb.orb.ORB_COLORS)))

    while True:
        # console prints
        if CLOCK.get_fps() < settings.REFRESH_RATE * 0.8:
            print 'fps: {}'.format(CLOCK.get_fps())

        # event handling
        # pressed = pygame.key.get_pressed()

        # # save states of alt, ctrl and shift key
        # alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        # ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        # shift_held = pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]

        # get integer with all the key mods, then use and operations to compare.
        key_mods = pygame.key.get_mods()
        # save states of alt, ctrl and shift key
        alt_held = key_mods & pygame.KMOD_ALT
        ctrl_held = key_mods & pygame.KMOD_CTRL
        shift_held = key_mods & pygame.KMOD_SHIFT

        for event in pygame.event.get():
            # exit if pressed on the X (top right)
            if event.type == pygame.QUIT:
                return
            # handel key presses
            elif event.type == pygame.KEYDOWN:
                # exit if press alt-f4 or ctrl-w
                if event.key == pygame.K_w and ctrl_held:
                    return
                elif event.key == pygame.K_F4 and alt_held:
                    return
                # other

        # game handling
        mouse_loc = pygame.mouse.get_pos()
        middle_loc = settings.WINDOW_CENTER
        new_angle = functions.incline_angle(mouse_loc, middle_loc)
        player.set_angle(new_angle, limit=playerSnake.playerSnake.MAX_ANGLE_CHANGE)
        player.move()

        for id_, obj in list(dataBase.iter_orbs()):
            collide = player.any_collide(obj)
            if collide:
                dataBase.remove_orb(id_)
                player.add_mass(obj.mass)

        # screen update
        rendering.set_camera_pos(player.get_location())
        rendering.set_zoom(20 / player.get_radius() + 1)
        rendering.render(display)
        pygame.display.flip()

        # tick timer
        CLOCK.tick(settings.REFRESH_RATE)


if __name__ == '__main__':
    main()

import pygame
import dataSets
import render
import snake
import playerSnake
import orb
import functions
import math


def main():
    pygame.init()
    display = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    board = pygame.Rect(0, 0, 9600, 5400)
    CLOCK = pygame.time.Clock()
    dataBase = dataSets.dataBase()
    rendering = render.render(display.get_rect(), board, dataBase)

    player = playerSnake.playerSnake((0, 0), 'nadav')
    dataBase.add_snake('1', player)

    while True:
        # console prints
        # print 'fps: {}'.format(CLOCK.get_fps())

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
        middle_loc = (960, 540)
        new_angle = functions.incline_angle(mouse_loc, middle_loc)
        player.set_angle(new_angle)  # , limit=math.radians(1.5)
        #player.move()
        player.relocate(mouse_loc)

        # screen update
        rendering.set_camera_pos(*player.get_location())
        rendering.set_zoom(1)
        rendering.render(display)
        pygame.display.flip()

        # tick timer
        CLOCK.tick(60)


if __name__ == '__main__':
    main()

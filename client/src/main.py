import pygame


def main():
    pygame.init()
    display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    CLOCK = pygame.time.Clock()

    quit_game = False

    while True:
        # console prints
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
                if event.key == pygame.K_F4 and alt_held:
                    return
                # other

        # game handling

        # screen update
        pygame.display.flip()

        # tick timer
        CLOCK.tick(60)


if __name__ == '__main__':
    main()

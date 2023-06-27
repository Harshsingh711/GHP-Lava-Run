import pygame
import pygame.mixer as mixer
from time import sleep

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

pygame.init()
mixer.init()
mixer.music.load("Itty Bitty 8 Bit.mp3")
mixer.music.set_volume(0.7)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    import menu
    import lava

    while True:
        menu.menu()
        lava.lava()

    # # sprite initialization
    # player.player(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
    # all_sprites = pygame.sprite.Group()
    # player = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    # all_sprites.add(player)

    # main while loop
    # running = True
    # while running:
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         running = False

        # all_sprites.update()

        # screen.fill((0, 0, 0))  # Fill the screen with black color
        # all_sprites.draw(screen)

        # pygame.display.flip()

# clock = pygame.time.Clock()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#     pygame.display.update()
#     clock.tick(60)

if __name__ == "__main__":
    main()
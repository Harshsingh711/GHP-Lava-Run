import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 1

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)


def player(screen, width, height):
    all_sprites = pygame.sprite.Group()
    player = Player(width/2, height/2)
    all_sprites.add(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        screen.fill((0, 0, 0))  # Fill the screen with black color
        all_sprites.draw(screen)

        pygame.display.flip()

    pygame.quit()
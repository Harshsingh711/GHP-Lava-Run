import pygame
import pygame.mixer as mixer
import time
import pygame as pg
import random

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)


def lava():
    from main import screen, SCREEN_HEIGHT, SCREEN_WIDTH

    mixer.music.play()
    pygame.display.set_caption("Moving Lava")

    # Lava properties
    lava_width = SCREEN_WIDTH
    lava_height = 50
    lava_x = 0
    lava_y = SCREEN_HEIGHT - lava_height
    lava_speed = 5

    # Game loop
    running = True
    clock = pygame.time.Clock()
    # sprite initialization
    player_pos = pygame.Vector2(1920 / 2, 1080 / 2 + 300)
    # player.Player(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
    # all_sprites = pygame.sprite.Group()
    # player = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    # all_sprites.add(player)

    acceleration = 1

    obstacle_width = 50
    obstacle_height = 20
    obstacle_x = 175
    obstacle_y = 0
    obstacle_speed = 5

    obstacles: list[tuple[pg.Rect]] = []
    tick_count: int = 0
    OBSTACLES_TICK_SPAWN: int = 900
    OBSTACLES_UPPER_LIMIT: int = 10

    start_time = time.time()

    while running:
        player_rect = pygame.Rect(player_pos.x - 20, player_pos.y - 20, 40, 40)
        if (
            tick_count % OBSTACLES_TICK_SPAWN == 0
            and len(obstacles) < OBSTACLES_UPPER_LIMIT
        ):
            while True:
                x = random.randint(0, SCREEN_WIDTH - obstacle_width)
                y = random.randint(100, SCREEN_HEIGHT - obstacle_height)
                rect = pg.Rect(
                    x,
                    y,
                    48 * random.randint(1, 3),
                    48 * random.randint(1, 3),
                )
                if not rect.colliderect(player_rect):
                    break
            obstacles.append(rect)

        clock.tick(60)  # Limit the frame rate to 60 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        obstacle_y += obstacle_speed

        # Check if obstacle is off-screen
        if obstacle_y > 1080:
            obstacle_y = 0

        # Draw the obstacle
        pygame.draw.rect(
            screen,
            (30, 40, 50),
            (obstacle_x, obstacle_y, obstacle_width, obstacle_height),
        )

        # Move the lava
        lava_y -= lava_speed * acceleration

        # Reset lava position if it goes off the screen
        if lava_y + lava_height < 0:
            lava_y = SCREEN_HEIGHT

        # Fill the screen with black color
        screen.fill(BLACK)

        # pygame.draw.rect(screen, "gray", , )

        pygame.draw.circle(screen, "white", player_pos, 20)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player_pos.y -= 75 * dt
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player_pos.y += 75 * dt
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player_pos.x -= 75 * dt
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player_pos.x += 75 * dt

        # obstacle
        for obs in obstacles:
            pg.draw.rect(screen, (30, 40, 50), obs)

        if pg.Rect.collidelist(player_rect, obstacles) != -1:
            running = False

        # Draw the lava
        lava = pygame.draw.rect(
            screen, RED, (lava_x, lava_y, lava_width, SCREEN_HEIGHT)
        )

        if lava.y <= player_pos.y + 15:
            break

        if player_pos.y < 100:
            lava_y = SCREEN_HEIGHT
            player_pos.y = 800
            player_pos.x = 640
            acceleration += 0.2
            OBSTACLES_TICK_SPAWN -= 50
            OBSTACLES_UPPER_LIMIT += 5
            obstacles.clear()

        if player_pos.x - 20 < 175:
            player_pos.x = 200
        if player_pos.x + 20 > SCREEN_WIDTH - 175:
            player_pos.x = SCREEN_WIDTH - 200

        dt = clock.tick(60) / 100

        pygame.display.update()
    screen.fill(BLACK)
    mixer.music.stop()

    duration = time.time() - start_time
    message = "Be better!" if duration < 30 else "Good job!"
    font = pygame.font.Font(None, 36)
    time_text = font.render(
        message + " You survived for "
        + str(round(time.time() - start_time, 2))
        + " seconds",
        True,
        RED,
    )
    w, h = time_text.get_size()
    cx, cy = screen.get_size()
    screen.blit(time_text, [cx // 2 - w // 2, cy // 2 - h // 2])
    
    names = [
        'Anish G.',
        'Yubo C.',
        'Harsh S.',
        'Sudeep P.'
    ]
    credit = ', '.join(names)
    credit_text = font.render(
        'Made by ' + credit,
        True,
        RED,
    )
    w, h = credit_text.get_size()
    cx, cy = screen.get_size()
    screen.blit(credit_text, [cx // 2 - w // 2, cy // 2 - h // 2 + 50])
    
    pygame.display.flip()
    time.sleep(5)

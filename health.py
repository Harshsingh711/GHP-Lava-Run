import pygame
from main import screen, SCREEN_HEIGHT, SCREEN_WIDTH

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

bar_width = 400
bar_height = 40
bar_x = (SCREEN_WIDTH - bar_width) // 2
bar_y = (SCREEN_HEIGHT - bar_height) // 2
max_health = 100
current_health = 100

# Animation properties
target_health = 0
tween_speed = 2

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if current_health != target_health:
        if current_health > target_health:
            current_health -= tween_speed
        else:
            current_health += tween_speed

        current_health = max(0, min(current_health, max_health))

    screen.fill(BLACK)

    pygame.draw.rect(screen, RED, (bar_x, bar_y, bar_width, bar_height))

    health_bar_width = int(bar_width * (current_health / max_health))

    pygame.draw.rect(screen, GREEN, (bar_x, bar_y, health_bar_width, bar_height))

    font = pygame.font.Font(None, 36)
    text = font.render(f"Health: {current_health}%", True, YELLOW)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))
    screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
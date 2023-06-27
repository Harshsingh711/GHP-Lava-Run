import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def menu():
    from main import screen, SCREEN_WIDTH, SCREEN_HEIGHT

    pygame.display.set_caption("Menu")
    
    # Button properties
    button_width = 200
    button_height = 50
    button_x = SCREEN_WIDTH // 2 - button_width // 2
    play_button_y = SCREEN_HEIGHT // 2 - button_height
    quit_button_y = SCREEN_HEIGHT // 2 + 50

    # Game loop
    running = True
    clock = pygame.time.Clock()

    # Fill the screen with black color
    screen.fill(BLACK)

    # Draw the game title
    title_font = pygame.font.Font(None, 172)
    title_text = title_font.render("LAVA RUN", True, RED)
    title_text_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 300))
    screen.blit(title_text, title_text_rect)

    # Draw the play button
    pygame.draw.rect(screen, WHITE, (button_x, play_button_y, button_width, button_height))
    play_text = pygame.font.Font(None, 36).render("Play", True, BLACK)
    play_text_rect = play_text.get_rect(center=(button_x + button_width // 2, play_button_y + button_height // 2))
    screen.blit(play_text, play_text_rect)

    # Draw the quit button
    pygame.draw.rect(screen, WHITE, (button_x, quit_button_y, button_width, button_height))
    quit_text = pygame.font.Font(None, 36).render("Quit", True, BLACK)
    quit_text_rect = quit_text.get_rect(center=(button_x + button_width // 2, quit_button_y + button_height // 2))
    screen.blit(quit_text, quit_text_rect)

    flag = False
    
    while running:
        clock.tick(60)  # Limit the frame rate to 60 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Check if play button is clicked
                if button_x <= mouse_pos[0] <= button_x + button_width:
                    if play_button_y <= mouse_pos[1] <= play_button_y + button_height:
                        # Start the game
                        flag = True

                # Check if quit button is clicked
                if button_x <= mouse_pos[0] <= button_x + button_width:
                    if quit_button_y <= mouse_pos[1] <= quit_button_y + button_height:
                        # Quit the game
                        pygame.quit()
                        sys.exit()

        
                # if button_x <= mouse_pos[0] <= button_x + button_width:
                #     if play_button_y <= mouse_pos[1] <= play_button_y + button_height:
                #         # Start the game
                #         os.system("python lava.py")  #Execute lava.py
                #         pygame.quit()
                #         sys.exit()
        if flag:
            break
        # Update the display
        pygame.display.flip()

    # Exit the menu
    screen.fill(BLACK)
    
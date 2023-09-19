import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jump King Clone - Menu")

# Create a font for text display
font = pygame.font.Font(None, 36)

# Menu variables
menu_active = True
player_name = ""



while menu_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and player_name:
                menu_active = False
            elif event.key == pygame.K_BACKSPACE:
                player_name = player_name[:-1]
            else:
                player_name += event.unicode

    # Draw the menu
    screen.fill(BLACK)
    title_text = font.render("Jump King Clone", True, WHITE)
    name_text = font.render("Enter Your Name:", True, WHITE)
    player_name_text = font.render(player_name, True, WHITE)
    start_text = font.render("Press Enter to Start", True, WHITE)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))
    screen.blit(name_text, (SCREEN_WIDTH // 2 - name_text.get_width() // 2, 250))
    screen.blit(player_name_text, (SCREEN_WIDTH // 2 - player_name_text.get_width() // 2, 300))
    screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, 400))
    pygame.display.flip()

# Start the game
import game  # Import your game.py script
game.start_game(player_name)

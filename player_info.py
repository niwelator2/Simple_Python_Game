import pygame
import sys

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Player Info Display")

# Load player icon image
player_icon = pygame.image.load("player.png")  # Replace with the path to your player icon image
player_icon = pygame.transform.scale(player_icon, (64, 64))  # Adjust the size as needed

# Create a font for displaying player info
font = pygame.font.Font(None, 36)

# Load player info from the "player_info.txt" file
player_info = []
try:
    with open("player_info.txt", "r") as file:
        for line in file:
            player_info.append(line.strip())
except FileNotFoundError:
    player_info = ["Player Info Not Found"]

# Menu variables
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the player info and icon
    screen.fill(BLACK)
    
    # Display player icon
    screen.blit(player_icon, (SCREEN_WIDTH // 2 - 32, SCREEN_HEIGHT // 2 - 64))

    # Display player info below the icon
    y = SCREEN_HEIGHT // 2 + 16
    for line in player_info:
        text = font.render(line, True, WHITE)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, y))
        y += 40  # Vertical spacing

    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()

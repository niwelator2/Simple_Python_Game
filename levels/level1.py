import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
FONT_SIZE = 24
TIMER_POS = (700, 20)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tutorial Level")

# Load background image
background_image = pygame.image.load("base.png")

# Initialize font and timer
font = pygame.font.Font(None, FONT_SIZE)
start_time = pygame.time.get_ticks()

# Tutorial text
tutorial_text = [
    "Welcome to the Tutorial Level!",
    "Rules:",
    "1. You can change your player's color.",
    "2. Race against time to complete the level.",
]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Display background image
    screen.blit(background_image, (0, 0))

    # Render tutorial text
    for i, line in enumerate(tutorial_text):
        text_surface = font.render(line, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, 100 + i * 30)
        screen.blit(text_surface, text_rect)

    # Calculate and render timer
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    timer_text = f"Timer: {elapsed_time} seconds"
    timer_surface = font.render(timer_text, True, (0, 0, 0))
    timer_rect = timer_surface.get_rect()
    timer_rect.topleft = TIMER_POS
    screen.blit(timer_surface, timer_rect)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Timer")

# Initialize variables
font = pygame.font.Font(None, FONT_SIZE)
timer_seconds = 0
is_running = False

# Function to format time
def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}:{minutes}:{seconds}"



# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_running:
                    is_running = False
                else:
                    is_running = True
            if event.key == pygame.K_r:
                timer_seconds = 0  # Reset timer when 'r' key is pressed

    # Update timer when it's running
    if is_running:
        timer_seconds += 1

    # Clear the screen
    screen.fill(WHITE)

    # Render and display timer
    timer_text = font.render(format_time(timer_seconds), True, BLACK)
    screen.blit(timer_text, (WIDTH // 2 - timer_text.get_width() // 2, HEIGHT // 2 - timer_text.get_height() // 2))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

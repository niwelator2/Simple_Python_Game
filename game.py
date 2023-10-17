import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 60, 70
PLATFORM_WIDTH, PLATFORM_HEIGHT = 50, 20
JUMP_HEIGHT = 15
GRAVITY = 0.5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jump King Clone")

# Load the player image
try:
    player_image = pygame.image.load("player.png").convert_alpha()
    player_image = pygame.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))
except pygame.error:
    print("Error loading player image.")
    sys.exit()

# Initialize player position and velocity
player_x = (WIDTH - PLAYER_WIDTH) // 2
player_y = HEIGHT - PLAYER_HEIGHT
player_velocity = 0
is_jumping = False

# Create platforms for the first level
platforms = [
    (200, 500),  # Ground platform
    (400, 500),  # Ground platform continuation
    (600, 500),  # Ground platform continuation
    (100, 300),  # Medium platform 1
    (350, 400),  # Medium platform 2
    (600, 300),  # Medium platform 3
    (300, 180),  # Low platform 1
    (500, 180),  # Low platform 2
    (400, 100),  # Low platform 3
    (200, 250),  # Medium platform 4
]

# Load the first background image
try:
    background_image = pygame.image.load("base.png")
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
except pygame.error:
    print("Error loading background image.")
    sys.exit()

# Set a flag for level transition
level_transition = False

# Initialize the game timer
font = pygame.font.Font(None, 36)
timer_seconds = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # player speed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 3
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_WIDTH:
        player_x += 3

    if not is_jumping:
        if keys[pygame.K_SPACE]:
            player_velocity = -JUMP_HEIGHT
            is_jumping = True

    player_velocity += GRAVITY
    player_y += player_velocity

    # Check if the player reaches a certain height to transition to level 2
    if player_y < 0 and not level_transition:
        level_transition = True

        # Load the second background image for level 2
        try:
            background_image = pygame.image.load("lv2.png")
            background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
        except pygame.error:
            print("Error loading background image for level 2.")
            sys.exit()

    # Set up platforms for level 2
    platforms = [
        (200, 500),  # Ground platform with obstacles
        (400, 500),  # Ground platform continuation
        (600, 500),  # Ground platform continuation
        (100, 300),  # Medium platform 1
        (350, 400),  # Medium platform 2
        (600, 300),  # Medium platform 3
        (300, 200),  # Low platform 1
        (500, 200),  # Low platform 2
        (400, 100),  # Low platform 3
        (200, 250),  # Medium platform 4
    ]

    # Check if the player reaches a certain height to transition to level 3
    if player_y < -200 and level_transition:
        level_transition = False  # Reset the transition flag

        # Load the third background image for level 3
        try:
            background_image = pygame.image.load("lv3.png")
            background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
        except pygame.error:
            print("Error loading background image for level 3.")
            sys.exit()
    # Set a flag for level transition
    level_transition = False
        # Set up platforms for level 3
    platforms = [
        (0, 500),
        (200, 500),  # Ground platform
        (400, 500),  # Ground platform continuation
        (600, 500),  # Ground platform continuation
        (150, 300),  # Floating platform 1
        (500, 300),  # Floating platform 2
        (300, 200),  # Floating platform 3
        (450, 100),  # Floating platform 4
        (100, 100),  # Floating platform 5
        (650, 50),   # Floating platform 6
        (200, 0),    # Ceiling platform
        (400, 0),    # Ceiling platform continuation
        (600, 0),    # Ceiling platform continuation
    ]
    # Check if the player collects the star
    star_image = pygame.image.load("star.png").convert_alpha()
    star_image = pygame.transform.scale(star_image, (50, 50))
    star_position = (400, 30)  # Adjust the star's position

    # Inside the game loop, after drawing the platforms, add the following code to display the star:
    screen.blit(star_image, star_position)

    # Check if the player collects the star
    star_position = (400, 30)  # Adjust the star's position
    if (
        player_x + PLAYER_WIDTH > star_position[0]
        and player_x < star_position[0] + 20
        and player_y < star_position[1] + 20
    ):
        # The player collected the star, end the game
        print("Congratulations! You collected the star and completed the game.")
        running = False

    for platform_x, platform_y in platforms:
        if (
            player_x < platform_x + PLAYER_WIDTH
            and player_x + PLAYER_WIDTH > platform_x
            and player_y + PLAYER_HEIGHT > platform_y
            and player_y + PLAYER_HEIGHT < platform_y + PLATFORM_HEIGHT
        ):
            player_velocity = 0
            is_jumping = False
            player_y = platform_y - PLAYER_HEIGHT

    if player_y > HEIGHT - PLAYER_HEIGHT:
        player_y = HEIGHT - PLAYER_HEIGHT
        is_jumping = False
        player_velocity = 0

    # Update and display the timer
    timer_seconds += 1
    timer_text = font.render(f"Time: {timer_seconds}", True, WHITE)

    screen.blit(background_image, (0, 0))

    for platform_x, platform_y in platforms:
        pygame.draw.rect(screen, (0, 255, 0), (platform_x, platform_y, PLATFORM_WIDTH, PLATFORM_HEIGHT))

    screen.blit(player_image, (player_x, player_y))

    # Display the timer in the top-right corner
    screen.blit(timer_text, (WIDTH - timer_text.get_width() - 10, 10))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

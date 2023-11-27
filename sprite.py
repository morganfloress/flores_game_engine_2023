import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 900, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("my game")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
brown = (165, 42, 42)

# Load background image
background_image_path = "mario_background.png"  # Replace with the correct path to your background image
background_image = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image, (width, height))

# Set up player
player_size = 30
player_x = width // 2 - player_size // 2
player_y = height - player_size - 20  # Adjusted starting position
player_speed = 10
jump_power = -20  # Increased jump height
gravity = 2
player_image_path = "R.png"  # Replace with the correct path to your image
player_image = pygame.image.load(player_image_path)
player_image = pygame.transform.scale(player_image, (player_size, player_size))

# Set up fixed platforms
platforms = [
    {"x": 70, "y": height - 100, "width": 200, "height": 10},
    {"x": 150, "y": height - 200, "width": 200, "height": 10},
    {"x": 250, "y": height - 300, "width": 200, "height": 10},
    {"x": 100, "y": height - 400, "width": 200, "height": 10},
    {"x": 300, "y": height - 500, "width": 200, "height": 10},
    {"x": 0, "y": height - 10, "width": width, "height": 10},  # Added bottom solid platform
]

# Set up score
score = 0
font = pygame.font.Font(None, 36)

# Set up player motion variables
player_y_velocity = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed

    # Check for collision with platforms
    on_platform = False
    for platform in platforms:
        if (
            player_x < platform["x"] + platform["width"]
            and player_x + player_size > platform["x"]
            and player_y + player_size > platform["y"]
            and player_y < platform["y"] + platform["height"]
        ):
            if keys[pygame.K_SPACE] and not on_platform:  # Only jump if the player is on a platform
                player_y_velocity = jump_power
                on_platform = True
            else:
                player_y = platform["y"] - player_size
                player_y_velocity = 0

    # Apply gravity
    player_y_velocity += gravity
    player_y += player_y_velocity

    # Clamp player position to screen boundaries
    player_y = max(0, min(player_y, height - player_size))

    screen.blit(background_image, (0, 0))  # Draw the background first

    # Draw player
    screen.blit(player_image, (player_x, player_y))

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, brown, (platform["x"], platform["y"], platform["width"], platform["height"]))

    # Draw score
    score_text = font.render("Score: {}".format(score), True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

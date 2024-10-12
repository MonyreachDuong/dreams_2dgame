import pygame
import sys

pygame.init()

# screen dimension
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

# color
SKY_BLUE = (135, 206, 235)
GROUND_BROWN = (139, 69, 19)
GROUND_GREEN = (34, 139, 34)
BLACK = (0, 0, 0)

# character
CHAR_HEIGHT = 40
CHAR_WIDTH = 40
CHAR_COLOR = BLACK
GRAVITY = 0.5
JUMP_STRENGTH = -10
JUMP_HEIGHT = (JUMP_STRENGTH ** 2) / (2 * GRAVITY)

# create and display screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Game")

# create ground and character
ground_rect = pygame.Rect(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50)
char_rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100 - CHAR_HEIGHT, CHAR_WIDTH, CHAR_HEIGHT)
char_velocity_y = 0
on_ground = True

# create platforms pattern
platforms = [] 
platform_movement = []
platform_width = 100
platform_height = 20
platform_spacing = JUMP_HEIGHT - 10  # Slightly less than max jump height to ensure reachability
initial_y = 450
level_height = 100  # Height between each level
horizontal_spacing = 200  # Increased horizontal spacing

for level in range(15):
    y = initial_y - level * level_height
    if level % 2 == 0:  # Even levels
       platform = pygame.Rect(SCREEN_WIDTH // 2 - platform_width // 2, y, platform_width, platform_height)
       platforms.append(platform)
       platform_movement.append(True)
    else:  # Odd levels
        platforms.append(pygame.Rect(SCREEN_WIDTH // 2 - platform_width // 2 - horizontal_spacing, y, platform_width, platform_height))
        platforms.append(pygame.Rect(SCREEN_WIDTH // 2 - platform_width // 2, y, platform_width, platform_height))
        platforms.append(pygame.Rect(SCREEN_WIDTH // 2 - platform_width // 2 + horizontal_spacing, y, platform_width, platform_height))
        platform_movement.append(False)
        platform_movement.append(False)
        platform_movement.append(False)

# game loop
running = True
camera_y = 0
platform_direction = 1
platform_speed = 3

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and char_rect.left > 0:
        char_rect.x -= 5
    if keys[pygame.K_RIGHT] and char_rect.right < SCREEN_WIDTH:
        char_rect.x += 5
    if keys[pygame.K_SPACE] and on_ground:
        char_velocity_y = JUMP_STRENGTH
        on_ground = False

    char_velocity_y += GRAVITY
    char_rect.y += char_velocity_y

    # Check for collision with ground
    if char_rect.colliderect(ground_rect):
        char_rect.bottom = ground_rect.top
        char_velocity_y = 0
        on_ground = True

    # Check for collision with platforms
    for platform in platforms:
        if char_rect.colliderect(platform) and char_velocity_y > 0:
            char_rect.bottom = platform.top
            char_velocity_y = 0
            on_ground = True

    for i, platform in enumerate(platforms):
        if platform_movement[i]:
            platform.x += platform_speed * platform_direction
            if platform.left < 0 or platform.right > SCREEN_WIDTH:
                platform_direction *= -1

    # Implement camera movement
    if char_rect.top < 150:
        camera_y = 150 - char_rect.top

    screen.fill(SKY_BLUE)

    # Draw ground
    ground_draw_rect = ground_rect.copy()
    ground_draw_rect.y += camera_y
    pygame.draw.rect(screen, GROUND_BROWN, ground_draw_rect)
    pygame.draw.line(screen, GROUND_GREEN, (0, SCREEN_HEIGHT - 50 + camera_y), (SCREEN_WIDTH, SCREEN_HEIGHT - 50 + camera_y), 5)

    # Draw character
    char_draw_rect = char_rect.copy()
    char_draw_rect.y += camera_y
    pygame.draw.rect(screen, CHAR_COLOR, char_draw_rect)

    # Draw platforms
    for platform in platforms:
        platform_draw_rect = platform.copy()
        platform_draw_rect.y += camera_y
        pygame.draw.rect(screen, GROUND_BROWN, platform_draw_rect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()

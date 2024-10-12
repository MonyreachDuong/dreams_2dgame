import pygame
import sys

pygame.init()

# screen dimension
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

# color
DARK_BLUE = (0, 0, 153)
GROUND_YELLOW = (255, 255, 153)
GROUND_PURPLE = (204, 204, 255)
WHITE = (255, 255, 255)

# character
CHAR_HEIGHT = 40
CHAR_WIDTH = 40
CHAR_COLOR = WHITE
GRAVITY = 0.5
JUMP_STRENGTH = -10

# create and display screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2d_game")

#create ground and character
ground_rect = pygame.Rect(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50)
char_rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100 - CHAR_HEIGHT, CHAR_WIDTH, CHAR_HEIGHT)
char_velocity_y = 0
on_ground = True

# pygame.Rect(x, y, width, height)

# create platforms
platforms = [
    pygame.Rect(200, 450, 100, 20), # platform1
    pygame.Rect(400, 350, 100, 20), # platform2
    pygame.Rect(600, 250, 100, 20), # platform3
    pygame.Rect(500, 150, 100, 20) # platform3
]

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and char_rect.left > 0:
        char_rect.x -= 5
    if keys[pygame.K_RIGHT] and char_rect.right > 0:
        char_rect.x += 5
    if keys[pygame.K_SPACE] and on_ground:
        char_velocity_y = JUMP_STRENGTH
        on_ground = False

    char_velocity_y += GRAVITY
    char_rect.y += char_velocity_y

    if char_rect.colliderect(ground_rect):
        char_rect.bottom = ground_rect.top
        char_velocity_y = 0
        on_ground = True

    if char_rect.left < 0:
        char_rect.left = 0
    if char_rect.right > SCREEN_WIDTH:
        char_rect.right = SCREEN_WIDTH
    if char_rect.top < 0:
        char_rect.top = 0
    if char_rect.bottom > SCREEN_HEIGHT - 50:
        char_rect.bottom = SCREEN_HEIGHT - 50

    for platform in platforms:
        if char_rect.colliderect(platform) and char_velocity_y > 0:
            char_rect.bottom = platform.top
            char_velocity_y = 0
            on_ground = True

    screen.fill(DARK_BLUE)

    pygame.draw.rect(screen, GROUND_YELLOW, ground_rect)
    pygame.draw.line(screen, GROUND_PURPLE, (0, SCREEN_HEIGHT - 50), (SCREEN_WIDTH, SCREEN_HEIGHT - 50), 5)

    pygame.draw.rect(screen, CHAR_COLOR, char_rect)

    for platform in platforms:
        pygame.draw.rect(screen, GROUND_YELLOW, platform)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
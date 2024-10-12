import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 400, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pygame Shapes')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define shapes' positions and sizes
square_pos = (100, 100)
square_size = 50

circle_pos = (300, 150)
circle_radius = 40

rect_pos = (280, 100)
rect_size = (120, 60)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with black
    screen.fill(BLACK)

    # Draw a square
    pygame.draw.rect(screen, RED, (square_pos[0], square_pos[1], square_size, square_size))

    # Draw a circle
    pygame.draw.circle(screen, GREEN, circle_pos, circle_radius)

    # Draw a rectangle
    pygame.draw.rect(screen, BLUE, (rect_pos[0], rect_pos[1], rect_size[0], rect_size[1]))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
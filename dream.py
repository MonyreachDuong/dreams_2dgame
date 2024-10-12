import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

# Colors
SKY_BLUE = (135, 206, 235)
GROUND_BROWN = (139, 69, 19)
GROUND_GREEN = (34, 139, 34)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255) 

# Character properties
CHAR_HEIGHT = 25
CHAR_WIDTH = 25
CHAR_COLOR = BLACK
GRAVITY = 0.5
JUMP_STRENGTH = -10
JUMP_HEIGHT = (JUMP_STRENGTH ** 2) / (2 * GRAVITY)

# Create and display screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dream")

# Load each background scene separately
background_scene1 = pygame.image.load("/Users/monyreach/Desktop/pygame/figma game assets/Backgroundscene1.png")
background_scene2 = pygame.image.load("/Users/monyreach/Desktop/pygame/figma game assets/Backgroundscene2.png")
background_scene3 = pygame.image.load("/Users/monyreach/Desktop/pygame/figma game assets/Backgroundscene3.png")
background_scene4 = pygame.image.load("/Users/monyreach/Desktop/pygame/figma game assets/Backgroundscene4.png")
background_scene5 = pygame.image.load("/Users/monyreach/Desktop/pygame/figma game assets/Backgroundscene5.png")
background_scene6 = pygame.image.load("/Users/monyreach/Desktop/pygame/figma game assets/Backgroundscene6.png")
background_scene7 = pygame.image.load("/Users/monyreach/Desktop/pygame/figma game assets/Backgroundscene7.png")

# Define the height for each scene
scene_heights = [600, 600, 600, 600, 600, 600, 900] 

# Scale each scene to fit the screen width and the specified height
background_scene1 = pygame.transform.scale(background_scene1, (SCREEN_WIDTH, scene_heights[0]))
background_scene2 = pygame.transform.scale(background_scene2, (SCREEN_WIDTH, scene_heights[1]))
background_scene3 = pygame.transform.scale(background_scene3, (SCREEN_WIDTH, scene_heights[2]))
background_scene4 = pygame.transform.scale(background_scene4, (SCREEN_WIDTH, scene_heights[3]))
background_scene5 = pygame.transform.scale(background_scene5, (SCREEN_WIDTH, scene_heights[4]))
background_scene6 = pygame.transform.scale(background_scene6, (SCREEN_WIDTH, scene_heights[5]))
background_scene7 = pygame.transform.scale(background_scene7, (SCREEN_WIDTH, scene_heights[6]))

# Calculate the vertical positions of each scene
total_height = sum(scene_heights)
scene_positions = [
    SCREEN_HEIGHT - scene_heights[0],  
    SCREEN_HEIGHT - sum(scene_heights[:2]),  
    SCREEN_HEIGHT - sum(scene_heights[:3]),  
    SCREEN_HEIGHT - sum(scene_heights[:4]),  
    SCREEN_HEIGHT - sum(scene_heights[:5]),
    SCREEN_HEIGHT - sum(scene_heights[:6]),
    SCREEN_HEIGHT - total_height, 
]

# Load and scale background image
menu_background = pygame.image.load("/Users/monyreach/Desktop/pygame/figma game assets/Menu_Screen.png")
menu_background = pygame.transform.scale(menu_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

leaderboard_background = pygame.image.load("/Users/monyreach/Desktop/pygame/figma game assets/Leaderboard.png")
leaderboard_background = pygame.transform.scale(leaderboard_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

enteryourname_background = pygame.image.load("/Users/monyreach/Desktop/pygame/figma game assets/Enter your name.png")
enteryourname_background = pygame.transform.scale(enteryourname_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

Congratulations_Screen = pygame.image.load("/Users/monyreach/Desktop/pygame/figma game assets/Congratulations_Screen.png")
Congratulations_Screen = pygame.transform.scale(Congratulations_Screen, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Define fonts
title_font = pygame.font.SysFont("Arial", 48)
button_font = pygame.font.SysFont("Arial", 36)
stats_font = pygame.font.SysFont("Arial", 28)

# Create ground and character
ground_rect = pygame.Rect(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50)
char_rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100 - CHAR_HEIGHT, CHAR_WIDTH, CHAR_HEIGHT)
char_velocity_y = 0
on_ground = True

# Manually defined platforms
platforms = [
    pygame.Rect(172, 465, 435, 27),  # Scene 1 Fixed platform
    pygame.Rect(85, 365, 105, 27),   # Scene 1 Fixed platform
    pygame.Rect(606, 365, 105, 27),  # Scene 1 Fixed platform
    pygame.Rect(286, 270, 209, 27),  # Scene 1 Nonfixed platform
    pygame.Rect(74, 180, 105, 27),  # Scene 1 Fixed platform
    pygame.Rect(606, 180, 105, 27),  # Scene 1 Fixed platform
    pygame.Rect(21, 80, 105, 27),  # Scene 1 Fixed platform
    pygame.Rect(671, 80, 105, 27),  # Scene 1 Fixed platform
    pygame.Rect(172, -40, 435, 27),  # Scene 2 Fixed platform
    pygame.Rect(286, -150, 209, 27),  # Scene 2 Nonfixed platform
    pygame.Rect(286, -275, 209, 27),  # Scene 2 Nonfixed platform
    pygame.Rect(286, -400, 209, 27),  # Scene 2 Nonfixed platform
    pygame.Rect(286, -525, 209, 27),  # Scene 2 Nonfixed platform
    pygame.Rect(463, -630, 105, 27),  # Scene 3 Fixed platform
    pygame.Rect(660, -750, 105, 27),  # Scene 3 Fixed platform
    pygame.Rect(600, -830, 105, 27),  # Scene 3 Fixed platform
    pygame.Rect(500, -910, 105, 27),  # Scene 3 Fixed platform
    pygame.Rect(65, -800, 105, 27),  # Scene 3 Fixed platform
    pygame.Rect(19, -880, 105, 27),  # Scene 3 Fixed platform
    pygame.Rect(70, -1000, 105, 27),  # Scene 3 Fixed platform
    pygame.Rect(165, -1120, 105, 27),  # Scene 3 Fixed platform
    pygame.Rect(237, -1250, 209, 27),  # Scene 4 Nonfixed platform
    pygame.Rect(0, -1400, 43, 112),  # Scene 4 Left Fixed platform
    pygame.Rect(94, -1450, 59, 16),  # Scene 4 Left Fixed platform
    pygame.Rect(7, -1550, 59, 16),  # Scene 4 Left Fixed platform
    pygame.Rect(66, -1650, 59, 16),  # Scene 4 Left Fixed platform
    pygame.Rect(150, -1750, 59, 16),  # Scene 4 Left Fixed platform
    pygame.Rect(700, -1400, 43, 112), # Scene 4 Right Fixed platform
    pygame.Rect(550, -1500, 59, 16),  # Scene 4 Right Fixed platform
    pygame.Rect(650, -1600, 59, 16),  # Scene 4 Right Fixed platform
    pygame.Rect(650, -1650, 59, 16),  # Scene 4 Right Fixed platform
    pygame.Rect(750, -1750, 59, 16),  # Scene 4 Right Fixed platform
    pygame.Rect(64, -1900, 105, 27),  # Scene 5 Fixed platform
    pygame.Rect(301, -1900, 105, 27),  # Scene 5 Fixed platform
    pygame.Rect(528, -1900, 105, 27),  # Scene 5 Fixed platform
    pygame.Rect(27, -2425, 19, 481),  # Scene 5 Fixed platform
    pygame.Rect(309, -2425, 19, 481),  # Scene 5 Fixed platform
    pygame.Rect(595, -2425, 19, 481),  # Scene 5 Fixed platform
    pygame.Rect(36, -2525, 59, 16),  # Scene 6 Fixed platform
    pygame.Rect(112, -2725, 43, 112),  # Scene 6  Fixed platform
    pygame.Rect(73, -2825, 105, 27),  # Scene 6  Fixed platform
    pygame.Rect(500, -2825, 43, 112),  # Scene 6  Fixed platform
    pygame.Rect(650, -2925, 59, 16),  # Scene 6 Fixed platform
    pygame.Rect(650, -3025, 59, 16),  # Scene 6 Fixed platform
    pygame.Rect(320, -3025, 59, 16),  # Scene 6 Fixed platform
    pygame.Rect(168, -3125, 39, 16),  # Scene 7 Fixed platform
    pygame.Rect(75, -3325, 43, 112),  # Scene 7  Fixed platform
    pygame.Rect(450, -3225, 39, 16),  # Scene 7 Fixed platform
    pygame.Rect(600, -3325, 39, 16),  # Scene 7 Fixed platform
    pygame.Rect(609, -3425, 39, 16),  # Scene 7 Fixed platform
    pygame.Rect(680, -3525, 39, 16),  # Scene 7 Fixed platform
    pygame.Rect(730, -3625, 39, 16),  # Scene 7 Fixed platform
    pygame.Rect(410, -3625, 39, 16),  # Scene 7 Fixed platform
    pygame.Rect(85, -3625, 39, 16),  # Scene 7 Fixed platform
    
]

# Define whether each platform is movable
platform_movement = [False, False, False, True, False, False, False, False, False, True, True, True, True, 
False, False, False, False, False, False, False, False, True, False, False, False, False, False, False,
False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
False, False, False, False, False, False, False, False, False, False]  

# Create a portal on a fixed platform at the top
portal_rect = pygame.Rect(0, -3725, 100, 20) 

# Game state
class GameState:
    MAIN_MENU = 1
    LEADERBOARD = 2
    USERNAME_INPUT = 3
    GAMEPLAY = 4
    GAME_COMPLETE = 5

current_state = GameState.MAIN_MENU
username = ""
start_time = None
elapsed_time = 0

# Button class
class Button:
    def __init__(self, text, x, y, width, height, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = WHITE
        self.callback = callback

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = button_font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.callback()

# Button callbacks
def start_game():
    global current_state, start_time, elapsed_time, char_rect, char_velocity_y, on_ground, camera_y
    
    if username:
        # Calculate the center position of the ground floor
        char_rect.x = (SCREEN_WIDTH // 2) - (CHAR_WIDTH // 2)
        char_rect.y = ground_rect.top - CHAR_HEIGHT
        
        # Reset game variables
        char_velocity_y = 0
        on_ground = True
        camera_y = 0

        current_state = GameState.GAMEPLAY
        start_time = pygame.time.get_ticks()
        elapsed_time = 0

def open_leaderboard():
    global current_state
    current_state = GameState.LEADERBOARD

def ask_username():
    global current_state, username
    username = ""
    current_state = GameState.USERNAME_INPUT

def back_to_menu():
    global current_state
    current_state = GameState.MAIN_MENU

def end_game():
    global current_state, elapsed_time, username, leaderboard_data
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000

    # Convert elapsed_time to "HH:MM:SS" format
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    time_str = f"{hours:02}:{minutes:02}:{seconds:02}"

    # Add the player's time to the leaderboard
    leaderboard_data.append((len(leaderboard_data) + 1, username, time_str))

    # Sort leaderboard by time, converting "HH:MM:SS" to total seconds for sorting
    def time_to_seconds(time_str):
        hours, minutes, seconds = map(int, time_str.split(":"))
        return hours * 3600 + minutes * 60 + seconds

    leaderboard_data.sort(key=lambda x: time_to_seconds(x[2]))

    # Update ranks
    for i in range(len(leaderboard_data)):
        leaderboard_data[i] = (i + 1, leaderboard_data[i][1], leaderboard_data[i][2])

    current_state = GameState.GAME_COMPLETE

# Create buttons
start_button = Button("Start Game", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 200, 50, ask_username)
leaderboard_button = Button("Leaderboard", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20, 200, 50, open_leaderboard)
ready_button = Button("Ready", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 50, start_game)
back_button = Button("Back", SCREEN_WIDTH - 120, 20, 100, 40, back_to_menu)
continue_button = Button("Continue", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 50, open_leaderboard)

# Example leaderboard data, replace with actual game data later
leaderboard_data = [
    (1, "Supreme", "00:00:45"),
    (2, "Champion", "00:00:55"),
    (3, "Master", "00:01:10"),
    (4, "Expert", "00:01:30"),
    (5, "Intermetdiate", "00:02:00"),
    (6, "Beginner", "00:03:00"),
    (7, "Noob", "00:05:00"),
    
]

# Game loop
running = True
camera_y = 0
platform_direction = 1
platform_speed = 3

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if current_state == GameState.MAIN_MENU:
                start_button.check_click(mouse_pos)
                leaderboard_button.check_click(mouse_pos)
            elif current_state == GameState.USERNAME_INPUT:
                ready_button.check_click(mouse_pos)
            elif current_state in (GameState.LEADERBOARD, GameState.GAME_COMPLETE, GameState.GAMEPLAY):
                back_button.check_click(mouse_pos)
                if current_state == GameState.GAME_COMPLETE:
                    continue_button.check_click(mouse_pos)
        elif event.type == pygame.KEYDOWN and current_state == GameState.USERNAME_INPUT:
            if event.key == pygame.K_BACKSPACE:
                username = username[:-1]
            elif event.key == pygame.K_RETURN and username:
                start_game()
            else:
                username += event.unicode

    if current_state == GameState.MAIN_MENU:
        # Draw main menu
        screen.blit(menu_background, (0, 0))

        # Draw buttons
        start_button.draw(screen)
        leaderboard_button.draw(screen)

    elif current_state == GameState.LEADERBOARD:
        # Draw leaderboard
        screen.blit(leaderboard_background, (0, 0))

        headers = ["No", "Username", "Time"]
        header_positions = [(SCREEN_WIDTH // 2 - 250, 200), (SCREEN_WIDTH // 2 - 100, 200), (SCREEN_WIDTH // 2 + 100, 200)]

        for i, header in enumerate(headers):
            header_surface = stats_font.render(header, True, BLACK)
            screen.blit(header_surface, header_positions[i])

        for idx, (rank, uname, time) in enumerate(leaderboard_data):
            rank_surface = stats_font.render(str(rank), True, BLACK)
            username_surface = stats_font.render(uname, True, BLACK)
            time_surface = stats_font.render(time, True, BLACK)

            screen.blit(rank_surface, (SCREEN_WIDTH // 2 - 250, 240 + 40 * idx))
            screen.blit(username_surface, (SCREEN_WIDTH // 2 - 100, 240 + 40 * idx))
            screen.blit(time_surface, (SCREEN_WIDTH // 2 + 100, 240 + 40 * idx))

        # Draw back button
        back_button.draw(screen)

    elif current_state == GameState.USERNAME_INPUT:
        # Draw username input
        
        screen.blit(enteryourname_background, (0, 0))
        username_surface = stats_font.render(username, True, BLACK)
        screen.blit(username_surface, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))

        # Draw ready button
        ready_button.draw(screen)

    elif current_state == GameState.GAMEPLAY:
        for i, scene in enumerate([background_scene1, background_scene2, background_scene3, 
                                   background_scene4, background_scene5, background_scene6, background_scene7]):
            screen.blit(scene, (0, scene_positions[i] + camera_y))

        # Game logic
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

        # Check for collision with portal
        if char_rect.colliderect(portal_rect):
            end_game()

        # Implement camera movement
        if char_rect.top < 150:
            camera_y = 150 - char_rect.top

        

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

        # Draw portal
        portal_draw_rect = portal_rect.copy()
        portal_draw_rect.y += camera_y
        pygame.draw.rect(screen, (255, 0, 0), portal_draw_rect)

        # Draw timer in "HH:MM:SS" format
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Convert to seconds
        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)
        timer_str = f"{hours:02}:{minutes:02}:{seconds:02}"
        timer_surface = stats_font.render(f"Time: {timer_str}", True, BLACK)
        screen.blit(timer_surface, (10, 10))

        # Draw back button
        back_button.draw(screen)

    elif current_state == GameState.GAME_COMPLETE:
        # Draw game complete screen
        screen.blit(Congratulations_Screen, (0, 0))
        message_surface = title_font.render(f"Congratulations, {username}!", True, BLACK)
        message_rect = message_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(message_surface, message_rect)

        time_surface = stats_font.render(f"You completed the maze in {timer_str} seconds", True, BLACK)
        time_rect = time_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(time_surface, time_rect)

        # Draw continue button
        continue_button.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()

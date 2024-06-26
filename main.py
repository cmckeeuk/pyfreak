import pygame
import random

print("loser freak weirdo")


# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 882
screen_height = 607
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Character Movement")

# Set up the character
character_width = 50
character_height = 50
character_x = screen_width // 2 - character_width // 2
character_y = screen_height // 2 - character_height // 2
pygame.draw.rect(screen, (0, 0, 255), (character_x, character_y, character_width, character_height), 5)
character_speed = 1



# Game loop
# Set up the enemies
enemy_width = 30
enemy_height = 30
enemy_x = [100, 200, 300]  # Initial x positions of enemies
enemy_y = [100, 200, 300]  # Initial y positions of enemies
enemy_speed = 5  # Speed of enemies

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update the screen
    screen.fill((40, 155, 60))  # Set the screen color to green
    # Draw grid lines
    grid_size = 55
    for x in range(0, screen_width, grid_size):
        pygame.draw.line(screen, (50, 255, 50), (x, 0), (x, screen_height))
        # Draw x-axis labels
        label = pygame.font.SysFont(None, 24).render(str(x // grid_size), True, (50, 255, 50))
        screen.blit(label, (x + 5, 5))
    for y in range(0, screen_height, grid_size):
        pygame.draw.line(screen, (50, 255, 50), (0, y), (screen_width, y))
        # Draw y-axis labels
        label = pygame.font.SysFont(None, 24).render(chr(ord('A') + y // grid_size), True, (50, 255, 50))
        screen.blit(label, (5, y + 5))
    # Select the part of the screen from the grid reference b1 to b4
    grid_size = 55

    # draw brown rectangle
    start_x = 2 * grid_size
    start_y = 2 * grid_size
    end_x = 5 * grid_size
    end_y = 3 * grid_size
    selected_area = pygame.Rect(start_x, start_y, end_x - start_x, end_y - start_y)
    pygame.draw.rect(screen, (139, 69, 19), selected_area, 50)

    # Store the previous position of the character
    prev_character_x = character_x
    prev_character_y = character_y

    # Draw the character
    pygame.draw.rect(screen, (155, 0, 100), (character_x, character_y, character_width, character_height))
    pygame.draw.rect(screen, (0, 0, 255), (character_x, character_y, character_width, character_height), 5)

    # Draw the enemies
    for i in range(len(enemy_x)):
        pygame.draw.rect(screen, (255, 180, 0), (enemy_x[i], enemy_y[i], enemy_width, enemy_height))
        # Check if character touches the enemy
        if character_x < enemy_x[i] + enemy_width and character_x + character_width > enemy_x[i] and character_y < enemy_y[i] + enemy_height and character_y + character_height > enemy_y[i]:
            # Reset the game
            character_x = screen_width // 2 - character_width // 2
            character_y = screen_height // 2 - character_height // 2
            enemy_x = [100, 200, 300]  # Reset enemy positions
            enemy_y = [100, 200, 300]
    pygame.display.flip()
    
    # Handle character movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
    if keys[pygame.K_RIGHT]:
        character_x += character_speed
    if keys[pygame.K_UP]:
        character_y -= character_speed
    if keys[pygame.K_DOWN]:
        character_y += character_speed
    if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
        character_x -= character_speed // 2
        character_y -= character_speed // 2
    if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
        character_x += character_speed // 2
        character_y -= character_speed // 2
    if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
        character_x -= character_speed // 2
        character_y += character_speed // 2
    if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
        character_x += character_speed // 2
        character_y += character_speed // 2

    # Check if character is hitting the wall
    if character_x < 0:
        character_x = 0
    if character_x > screen_width - character_width:
        character_x = screen_width - character_width

    if character_y < 0:
        character_y = 0
    if character_y > screen_height - character_height:
        character_y = screen_height - character_height

    # Check if character is hitting the wall or the brown rectangle
    if screen.get_at((character_x + character_width -1, character_y + character_height -1)) == (139, 69, 19):
        character_x = prev_character_x
        character_y = prev_character_y

    if screen.get_at((character_x, character_y + character_height - 1)) == (139, 69, 19):
        character_x = prev_character_x
        character_y = prev_character_y

    if screen.get_at((character_x + character_width -1, character_y)) == (139, 69, 19):
        character_x = prev_character_x
        character_y = prev_character_y

    if screen.get_at((character_x, character_y)) == (139, 69, 19):
        character_x = prev_character_x
        character_y = prev_character_y

    # Update enemy positions
    for i in range(len(enemy_x)):
        # Randomly move the enemies
        direction = random.choice(["left", "right", "up", "down"])
        if direction == "left":
            enemy_x[i] -= enemy_speed
            if enemy_x[i] < 0:
                enemy_x[i] = 0
            if enemy_x[i] > screen_width - enemy_width:
                enemy_x[i] = screen_width - enemy_width
            if enemy_y[i] < 0:
                enemy_y[i] = 0
            if enemy_y[i] > screen_height - enemy_height:
                enemy_y[i] = screen_height - enemy_height
            if random.randint(0, 100) < 5:
                direction = random.choice(["left", "right", "up", "down"])
                if direction == "left":
                    enemy_x[i] -= enemy_speed
                elif direction == "right":
                    enemy_x[i] += enemy_speed
                elif direction == "up":
                    enemy_y[i] -= enemy_speed
                elif direction == "down":
                    enemy_y[i] += enemy_speed
                   
        elif direction == "right":
            enemy_x[i] += enemy_speed
        elif direction == "up":
            enemy_y[i] -= enemy_speed
        elif direction == "down":
            enemy_y[i] += enemy_speed
        # Check if enemy is hitting the wall
        if enemy_x[i] < 0:
            enemy_x[i] = 0
        if enemy_x[i] > screen_width - enemy_width:
            enemy_x[i] = screen_width - enemy_width
        if enemy_y[i] < 0:
            enemy_y[i] = 0
        if enemy_y[i] > screen_height - enemy_height:
            enemy_y[i] = screen_height - enemy_height
# Quit the game
pygame.quit()
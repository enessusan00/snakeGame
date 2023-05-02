import pygame
import time
import random
pygame.init()

# Set the game window size
display_width = 800
display_height = 600

# Set the game caption
pygame.display.set_caption('Snake Game')
# Create the game window
game_display = pygame.display.set_mode((display_width, display_height))

# Set the background color to white
white = (255, 255, 255)
game_display.fill(white)
# Set up the game loop
game_over = False
while not game_over:
    # Handle game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    # Update game state
    
    # Draw game elements
    
    # Update the game display
    pygame.display.update()
# Create the snake
snake_block_size = 10
snake_speed = 15
snake_list = []
snake_length = 1
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, black, [x[0], x[1], snake_block_size, snake_block_size])
# Move the snake
def move_snake(snake_block_size, snake_list, direction):
    if direction == "right":
        head = [snake_list[0][0] + snake_block_size, snake_list[0][1]]
    elif direction == "left":
        head = [snake_list[0][0] - snake_block_size, snake_list[0][1]]
    elif direction == "up":
        head = [snake_list[0][0], snake_list[0][1] - snake_block_size]
    elif direction == "down":
        head = [snake_list[0][0], snake_list[0][1] + snake_block_size]
    snake_list.insert(0, head)
    snake_list.pop()
# Create the food
food_block_size = 10
food_x = round(random.randrange(0, display_width - food_block_size) / 10.0) * 10.0
food_y = round(random.randrange(0, display_height - food_block_size) / 10.0) * 10.0

def draw_food(food_x, food_y, food_block_size):
    pygame.draw.rect(game_display, red, [food_x, food_y, food_block_size, food_block_size])
# Check for collisions
def check_collisions(snake_head, snake_list, display_width, display_height):
    if snake_head[0] >= display_width or snake_head[0] < 0 or snake_head[1] >= display_height or snake_head[1] < 0:
        return True
    for block in snake_list[1:]:
        if snake_head == block:
            return True
    return False
# Set up the game loop
game_over = False
direction = "right"
snake_list = [[display_width / 2, display_height / 2]]
snake_length = 1
while not game_over:
    # Handle game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = "left"
            elif event.key == pygame.K_RIGHT:
                direction = "right"
            elif event.key == pygame.K_UP:
                direction = "up"
            elif event.key == pygame.K_DOWN:
                direction = "down"
    
    # Move the snake
    move_snake(snake_block_size, snake_list, direction)
    
    # Check for collisions
    snake_head = snake_list[0]
    if check_collisions(snake_head, snake_list, display_width, display_height):
        game_over = True
    
    # Check if the snake has eaten the food
    if snake_head[0] == food_x and snake_head[1] == food_y:
        food_x = round(random.randrange(0, display_width - food_block_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, display_height - food_block_size) / 10.0) * 10.0
        snake_length += 1
    
    # Draw game elements
    game_display.fill(white)
    draw_snake(snake_block_size, snake_list)
    draw_food(food_x, food_y, food_block_size)
    
    # Update the game display
    pygame.display.update()
    
    # Set the game speed
    clock = pygame.time.Clock()
    clock.tick(snake_speed)
    
# Quit Pygame
pygame.quit()
quit()

import pygame
import time
import random

# Initialize the game
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

# Set the width and height of the game window
window_width = 800
window_height = 600

# Set the size of each snake segment and the speed of the snake
segment_size = 20
snake_speed = 15

# Create the game window
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# Create a clock object to control the game's frame rate
clock = pygame.time.Clock()

# Define the font for displaying the score
font_style = pygame.font.SysFont(None, 50)

# Function to display the score on the game window
def show_score(score):
    score_text = font_style.render("Score: " + str(score), True, black)
    game_window.blit(score_text, [10, 10])

# Function to create the snake
def create_snake(segment_size, snake_list):
    for segment in snake_list:
        pygame.draw.rect(game_window, green, [segment[0], segment[1], segment_size, segment_size])

# Function to run the game
def run_game():
    game_over = False
    game_close = False

    # Initialize the starting position of the snake
    x1 = window_width / 2
    y1 = window_height / 2

    # Initialize the change in position of the snake
    x1_change = 0
    y1_change = 0

    # Create the initial snake with 1 segment
    snake_list = []
    snake_length = 1

    # Generate the initial food position
    food_x = round(random.randrange(0, window_width - segment_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, window_height - segment_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            game_window.fill(white)
            game_over_text = font_style.render("Game Over", True, red)
            game_window.blit(game_over_text, [window_width / 2.7, window_height / 3])
            show_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        run_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -segment_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = segment_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -segment_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = segment_size
                    x1_change = 0

        # Check if the snake collides with the boundaries of the game window
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change
        game_window.fill(white)

        # Draw the food
        pygame.draw.rect(game_window, red, [food_x, food_y, segment_size, segment_size])

        # Update the snake's length and position
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if the snake collides with itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Create the snake
        create_snake(segment_size, snake_list)

        # Update the score
        show_score(snake_length - 1)

        # Update the game window
        pygame.display.update()

        # Check if the snake eats the food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, window_width - segment_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, window_height - segment_size) / 20.0) * 20.0
            snake_length += 1

        # Control the speed of the snake
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Run the game
run_game()





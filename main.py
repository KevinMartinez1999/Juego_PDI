import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the display
tam_screen = (1280, 600)
screen = pygame.display.set_mode(tam_screen)
pygame.display.set_caption('Football Head')

# Load images
background_img = pygame.image.load('images/background.png')
player1_img = pygame.image.load('images/player1.png')
player2_img = pygame.image.load('images/player2.png')
ball_img = pygame.image.load('images/ball.png')
porteria1_img = pygame.image.load('images/porteria1.png')
porteria2_img = pygame.image.load('images/porteria2.png')

# Resize porteria
porteria_size = (200, 250)
porteria1_img = pygame.transform.scale(porteria1_img, porteria_size)
porteria2_img = pygame.transform.scale(porteria2_img, porteria_size)

# Resize players
player_size = (100, 100)
player1_img = pygame.transform.scale(player1_img, player_size)
player2_img = pygame.transform.scale(player2_img, player_size)

# Resize ball
ball_size = (50, 50)
ball_img = pygame.transform.scale(ball_img, ball_size)

# Resize background
background_img = pygame.transform.scale(background_img, tam_screen)

# Flag of collition
flag_collition = 0

# Set up game objects
porteria1_rect = porteria1_img.get_rect()
porteria1_rect.x = 0
porteria1_rect.y = 270

porteria2_rect = porteria2_img.get_rect()
porteria2_rect.x = 1080
porteria2_rect.y = 270

player1_rect = player1_img.get_rect()
player1_rect.x = 200
player1_rect.y = 400

player2_rect = player2_img.get_rect()
player2_rect.x = 970
player2_rect.y = 400

ball_rect = ball_img.get_rect()

# Set up game variables
player1_speed = 1.0
player2_speed = 1.0

v0 = 80.0
theta = 60.0
g = 9.8
t = 0.0

x0 = 600
y0 = 100

v0x = v0 * np.cos(np.deg2rad(theta))
v0y = v0 * np.sin(np.deg2rad(theta))

# Set up game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move players
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if player1_rect.x > 150:
            player1_rect.x -= player1_speed
    if keys[pygame.K_d]:
        if player1_rect.x < 1030:
            player1_rect.x += player1_speed
    if keys[pygame.K_LEFT]:
        if player2_rect.x > 150:
            player2_rect.x -= player2_speed
    if keys[pygame.K_RIGHT]:
        if player2_rect.x < 1030:
            player2_rect.x += player2_speed
    
    # Move ball
    t += 0.01
    X = v0x * t
    Y = v0y * t + 0.5 * g * t**2

    ball_rect.x = x0 + X
    ball_rect.y = y0 + Y

    # Detect collisions
    if ball_rect.bottom > tam_screen[1]-100:
        v0y *= -1
        t = 0.0
        y0 = ball_rect.y
        x0 = ball_rect.x
    elif ball_rect.top < 0:
        v0y *= -1
        t = 0.0
        y0 = ball_rect.y
        x0 = ball_rect.x
    elif ball_rect.right > tam_screen[0]:
        v0x *= -1
        t = 0.0
        y0 = ball_rect.y
        x0 = ball_rect.x
    elif ball_rect.left < 0:
        v0x *= -1
        t = 0.0
        y0 = ball_rect.y
        x0 = ball_rect.x

    # Draw objects
    screen.blit(background_img, (0, 0))
    screen.blit(player1_img, player1_rect)
    screen.blit(player2_img, player2_rect)
    screen.blit(ball_img, ball_rect)
    screen.blit(porteria1_img, porteria1_rect)
    screen.blit(porteria2_img, porteria2_rect)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

import pygame

# Initialize Pygame
pygame.init()

# Set up the display
tam_screen = (800, 600)
screen = pygame.display.set_mode(tam_screen)
pygame.display.set_caption('Football Head')

# Load images
background_img = pygame.image.load('images/background.png')
player1_img = pygame.image.load('images/player1.png')
player2_img = pygame.image.load('images/player2.png')
ball_img = pygame.image.load('images/ball.png')

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
player1_rect = player1_img.get_rect()
player1_rect.x = 100
player1_rect.y = 450

player2_rect = player2_img.get_rect()
player2_rect.x = 600
player2_rect.y = 450

ball_rect = ball_img.get_rect()
ball_rect.x = 400
ball_rect.y = 300

# Set up game variables
player1_speed = 5
player2_speed = 5

ball_speed_x = 5
ball_speed_y = 5

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
        if player1_rect.x > 0:
            player1_rect.x -= player1_speed
    if keys[pygame.K_d]:
        if player1_rect.x < 700:
            player1_rect.x += player1_speed
    if keys[pygame.K_LEFT]:
        if player2_rect.x > 0:
            player2_rect.x -= player2_speed
    if keys[pygame.K_RIGHT]:
        if player2_rect.x < 700:
            player2_rect.x += player2_speed
    
    # Move ball
    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y

    # Detect collisions
    if ball_rect.colliderect(player1_rect):
        if flag_collition == 0:
            ball_speed_x *= -1
            flag_collition = 1
    elif ball_rect.colliderect(player2_rect):
        if flag_collition == 0:
            ball_speed_x *= -1
            flag_collition = 1
    else:
        flag_collition = 0
    if ball_rect.top < 0 or ball_rect.bottom > tam_screen[1]:
        ball_speed_y *= -1
    if ball_rect.left < 0 or ball_rect.right > tam_screen[0]:
        ball_speed_x *= -1

    # Draw objects
    screen.blit(background_img, (0, 0))
    screen.blit(player1_img, player1_rect)
    screen.blit(player2_img, player2_rect)
    screen.blit(ball_img, ball_rect)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

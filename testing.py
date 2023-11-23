import pygame

# Setup
pygame.init()   #initialize pygame
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)   #set the screen to these dimensions
clock = pygame.time.Clock()     #set the clock to the pygame clock
running = True      # set the state of the game running to true
dt = 0.05

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# GAME LOOP
while (running):
    # Waiting for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # This is when a user clicks the x, stop the game loop by changing running to false
            running = False
    
    # This will fill the screen to a color to wipe away the last frame
    screen.fill("grey")

    # GAME RENDERING HERE
    # How to draw shapes:
    circle = pygame.draw.circle(screen, "red", player_pos, 40)

    #How to get key inputs:
    keys = pygame.key.get_pressed()

    
    # if circle.right > width:
    #     player_pos.x = width
    # if circle.top < 0:
    #     player_pos.y = 0
    # if circle.bottom > height:
    #     player_pos.y = height

    if keys[pygame.K_w]:
        if circle.bottom > height:
            player_pos.y = height
        else:
            player_pos.y -= 300 * dt
    elif keys[pygame.K_UP]:
        if circle.bottom > height:
            player_pos.y = height
        else:
            player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    elif keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    elif keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    elif keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt

    
    
    
    # Display work on screen
    pygame.display.flip()

    # Set the FPS to 60FPS
    clock.tick(60)

pygame.quit()
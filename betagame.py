import random, pygame as pg, sys

pg.init()

SIZE = (WIDTH, HEIGHT) = (1280, 720)
screen = pg.display.set_mode(SIZE)
clock = pg.time.Clock()     #set the clock to the pygame clock
projectile_left = projectile_right = projectile_top = projectile_bottom = False
projectile_radius = 30
score = 0
font = pg.font.Font('freesansbold.ttf', 30)

colors = (
    pg.Color("red"), pg.Color("yellow"), pg.Color("blue"),
    pg.Color("cyan"), pg.Color("green"), pg.Color("purple")
)

player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# GAME LOOP
while True:
    # Waiting for events
    for event in pg.event.get():
        if event.type == pg.QUIT:   # This is when a user clicks the x, stop the game loop by changing running to false
            pg.quit()
            sys.exit()

    # This will fill the screen to a color to wipe away the last frame
    screen.fill("grey")

    # GAME RENDERING HERE
    # How to draw shapes:
    player = pg.draw.circle(screen, "red", player_pos, 40)
    # player_rect = pg

    #How to get key inputs:
    keys = pg.key.get_pressed()

    move = 15 if keys[pg.K_LSHIFT] or keys[pg.K_RSHIFT] else 10

    if keys[pg.K_ESCAPE]:
        pg.quit()
        sys.exit()
    if keys[pg.K_w] or keys[pg.K_UP]:
        player_pos.y -= move
    if keys[pg.K_s] or keys[pg.K_DOWN]:
        player_pos.y += move
    if keys[pg.K_a] or keys[pg.K_LEFT]:
        player_pos.x -= move
    if keys[pg.K_d] or keys[pg.K_RIGHT]:
        player_pos.x += move
    if player.top < 0:
        player_pos.y = 0
    if player.bottom > HEIGHT:
        player_pos.y = HEIGHT - player.h
    if player.left < 0:
        player_pos.x = 0
    if player.right > WIDTH:
        player_pos.x = WIDTH - player.w
    

    # PROJECTILES
    if projectile_left == False:
        score += 1
        projectile_left_pos = (0,random.randint(0, HEIGHT))
        circle_left = pg.draw.circle(screen, "blue", projectile_left_pos, projectile_radius)
        projectile_left = True
    elif projectile_left == True:
        projectile_left_pos = (projectile_left_pos[0] + (WIDTH/100), projectile_left_pos[1])
        circle_left = pg.draw.circle(screen, "blue", projectile_left_pos, projectile_radius)
        if projectile_left_pos[0] > WIDTH:
            projectile_left = False
    
    if projectile_right == False:
        projectile_right_pos = (WIDTH,random.randint(0, HEIGHT))
        circle_right = pg.draw.circle(screen, "blue", projectile_right_pos, projectile_radius)
        projectile_right = True
    elif projectile_right == True:
        projectile_right_pos = (projectile_right_pos[0] - (WIDTH/100), projectile_right_pos[1])
        circle_right = pg.draw.circle(screen, "blue", projectile_right_pos, projectile_radius)
        if projectile_right_pos[0] < 0:
            projectile_right = False

    if projectile_top == False:
        projectile_top_pos = (random.randint(0, WIDTH),0)
        circle_top = pg.draw.circle(screen, "blue", projectile_top_pos, projectile_radius)
        projectile_top = True
    elif projectile_top == True:
        projectile_top_pos = (projectile_top_pos[0], projectile_top_pos[1]+(HEIGHT/100))
        circle_top = pg.draw.circle(screen, "blue", projectile_top_pos, projectile_radius)
        if projectile_top_pos[1] > HEIGHT:
            projectile_top = False

    if projectile_bottom == False:
        projectile_bottom_pos = (random.randint(0, WIDTH),HEIGHT)
        circle_bottom = pg.draw.circle(screen, "blue", projectile_bottom_pos, projectile_radius)
        projectile_bottom = True
    elif projectile_bottom == True:
        projectile_bottom_pos = (projectile_bottom_pos[0], projectile_bottom_pos[1]-(HEIGHT/100))
        circle_bottom = pg.draw.circle(screen, "blue", projectile_bottom_pos, projectile_radius)
        if projectile_bottom_pos[1] < 0:
            projectile_bottom = False

    collide = player.collidelist([circle_left, circle_right, circle_top, circle_bottom])

    print(collide)

    if not (collide == -1):
        score = 0

    text = font.render("Score {0}".format(score), True, "black")
    screen.blit(text, (WIDTH/2 - 20,20))

    
    
    # Display work on screen
    pg.display.flip()

    # Set the FPS to 60FPS
    clock.tick(60)

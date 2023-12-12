import random, pygame as pg, sys
from button import Button

pg.init()

# SCREEN SETTINGS
SIZE = (WIDTH, HEIGHT) = (1280, 720)
screen = pg.display.set_mode(SIZE)
clock = pg.time.Clock()     #set the clock to the pygame clock
CURRENT_SCREEN = "Main Menu"

# Projectiles initial settings
projectile_left = projectile_right = projectile_top = projectile_bottom = False
projectile_left_pos = (0,0)
projectile_right_pos = (WIDTH,0)
projectile_top_pos = (0,0)
projectile_bottom_pos = (0,HEIGHT)
projectile_radius = 30
projectile_X_init_speed = WIDTH/100
projectile_Y_init_speed = HEIGHT/100
collect_projectile = False
collect_projectile_axis = 1

player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# SCORE STARE VARIABLES
score = 0
SCORES = [0,0,0,0,0]
CLASSIC_OP_SCORES = [0,0,0,0,0]
CLASSIC_TP_SCORES = [0,0,0,0,0]
CLASSIC_VS_SCORES = [0,0,0,0,0]
COLLECT_OP_SCORES = [0,0,0,0,0]
COLLECT_TP_SCORES = [0,0,0,0,0]
COLLECT_VS_SCORES = [0,0,0,0,0]
CHALLENGE_OP_SCORES = [0,0,0,0,0]
CHALLENGE_TP_SCORES = [0,0,0,0,0]
CHALLENGE_VS_SCORES = [0,0,0,0,0]

# GAME SETTINGS
MUTED = False
DIFFICULTY_SETTING = "Medium"
GAMEMODE = "Classic"
NUM_PLAYERS = "1-Player"

# For 2 player mode
player1_pos = pg.Vector2(WIDTH/3, HEIGHT/2)
player2_pos = pg.Vector2(WIDTH/1.5, HEIGHT/2)
player1_alive = player2_alive = True
score_p1_collide = score_p2_collide = 0

# FONTS
font = pg.font.Font('freesansbold.ttf', 30)
header_font = pg.font.Font('freesansbold.ttf', 60)

###################################################################################################################
# HELPER FUNCTIONS
###################################################################################################################

def check_exit_pygame_menu(event):
    if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
    elif event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
            pg.quit()
            sys.exit()   

def check_exit(event):
    if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
            
def handle_movement(player = None, player1 = None, player2 = None):
    keys = pg.key.get_pressed()

    if NUM_PLAYERS == "1-Player":
        move = 15 if keys[pg.K_LSHIFT] or keys[pg.K_RSHIFT] else 10
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
    else:
        move_player1 = 15 if keys[pg.K_LSHIFT] else 10
        move_player2 = 15 if keys[pg.K_RSHIFT] else 10
        if player1 != None:
            if keys[pg.K_w]:
                player1_pos.y -= move_player1
            if keys[pg.K_s]:
                player1_pos.y += move_player1
            if keys[pg.K_a]:
                player1_pos.x -= move_player1
            if keys[pg.K_d]:
                player1_pos.x += move_player1
            if player1.top < 0:
                player1_pos.y = 0
            if player1.bottom > HEIGHT:
                player1_pos.y = HEIGHT - player1.h
            if player1.left < 0:
                player1_pos.x = 0
            if player1.right > WIDTH:
                player1_pos.x = WIDTH - player1.w
        # PLAYER 2
        if player2 != None:
            if keys[pg.K_UP]:
                player2_pos.y -= move_player2
            if keys[pg.K_DOWN]:
                player2_pos.y += move_player2
            if keys[pg.K_LEFT]:
                player2_pos.x -= move_player2
            if keys[pg.K_RIGHT]:
                player2_pos.x += move_player2
            if player2.top < 0:
                player2_pos.y = 0
            if player2.bottom > HEIGHT:
                player2_pos.y = HEIGHT - player2.h
            if player2.left < 0:
                player2_pos.x = 0
            if player2.right > WIDTH:
                player2_pos.x = WIDTH - player2.w

def generate_hazards_classic():
    global projectile_left, projectile_right, projectile_top, projectile_bottom, projectile_left_pos, projectile_right_pos, projectile_top_pos, projectile_bottom_pos, projectile_radius, projectile_X_init_speed, projectile_Y_init_speed
    if GAMEMODE == "Classic":
        projectile_radius = 30 if DIFFICULTY_SETTING == "Medium" else 20 if DIFFICULTY_SETTING == "Easy" else 35
    if GAMEMODE == "Collect":
        projectile_radius = 30 if DIFFICULTY_SETTING == "Medium" else 20 if DIFFICULTY_SETTING == "Hard" else 35
    projectile_X_init_speed = WIDTH/100 if DIFFICULTY_SETTING == "Medium" else WIDTH/150 if DIFFICULTY_SETTING == "Easy" else WIDTH/75
    projectile_Y_init_speed = HEIGHT/100 if DIFFICULTY_SETTING == "Medium" else HEIGHT/150 if DIFFICULTY_SETTING == "Easy" else HEIGHT/75
    if projectile_left == False:
        projectile_left_pos = (0,random.randint(0, HEIGHT))
        circle_left = pg.draw.circle(screen, "blue", projectile_left_pos, projectile_radius)
        projectile_left = True
    elif projectile_left == True:
        projectile_left_pos = (projectile_left_pos[0] + projectile_X_init_speed, projectile_left_pos[1])
        circle_left = pg.draw.circle(screen, "blue", projectile_left_pos, projectile_radius)
        if projectile_left_pos[0] > WIDTH:
            projectile_left = False
    
    if projectile_right == False:
        projectile_right_pos = (WIDTH,random.randint(0, HEIGHT))
        circle_right = pg.draw.circle(screen, "blue", projectile_right_pos, projectile_radius)
        projectile_right = True
    elif projectile_right == True:
        projectile_right_pos = (projectile_right_pos[0] - projectile_X_init_speed, projectile_right_pos[1])
        circle_right = pg.draw.circle(screen, "blue", projectile_right_pos, projectile_radius)
        if projectile_right_pos[0] < 0:
            projectile_right = False

    if projectile_top == False:
        projectile_top_pos = (random.randint(0, WIDTH),0)
        circle_top = pg.draw.circle(screen, "dark blue", projectile_top_pos, projectile_radius)
        projectile_top = True
    elif projectile_top == True:
        projectile_top_pos = (projectile_top_pos[0], projectile_top_pos[1]+projectile_Y_init_speed)
        circle_top = pg.draw.circle(screen, "dark blue", projectile_top_pos, projectile_radius)
        if projectile_top_pos[1] > HEIGHT:
            projectile_top = False

    if projectile_bottom == False:
        projectile_bottom_pos = (random.randint(0, WIDTH),HEIGHT)
        circle_bottom = pg.draw.circle(screen, "dark blue", projectile_bottom_pos, projectile_radius)
        projectile_bottom = True
    elif projectile_bottom == True:
        projectile_bottom_pos = (projectile_bottom_pos[0], projectile_bottom_pos[1]-projectile_Y_init_speed)
        circle_bottom = pg.draw.circle(screen, "dark blue", projectile_bottom_pos, projectile_radius)
        if projectile_bottom_pos[1] < 0:
            projectile_bottom = False
    
    return [circle_left, circle_right, circle_top, circle_bottom]

def generate_collect_mode_hazard():
    global collect_projectile, projectile_pos, projectile_radius, projectile_X_init_speed, projectile_Y_init_speed, collect_projectile_axis
    projectile_radius = 30 if DIFFICULTY_SETTING == "Medium" else 20 if DIFFICULTY_SETTING == "Easy" else 35
    projectile_X_init_speed = WIDTH/100 if DIFFICULTY_SETTING == "Medium" else WIDTH/150 if DIFFICULTY_SETTING == "Easy" else WIDTH/75
    projectile_Y_init_speed = HEIGHT/100 if DIFFICULTY_SETTING == "Medium" else HEIGHT/150 if DIFFICULTY_SETTING == "Easy" else HEIGHT/75
    if collect_projectile == False:
        collect_projectile_axis = random.randint(1,4)

    if collect_projectile == False and collect_projectile_axis == 1:
        projectile_pos = (0,random.randint(0, HEIGHT))
        projectile_square = pg.draw.rect(screen, "black", pg.Rect(projectile_pos[0], projectile_pos[1], projectile_radius * 2.2, projectile_radius * 2.2))
        collect_projectile = True
    elif collect_projectile == True and collect_projectile_axis == 1:
        projectile_pos = (projectile_pos[0] + projectile_X_init_speed, projectile_pos[1])
        projectile_square = pg.draw.rect(screen, "black", pg.Rect(projectile_pos[0], projectile_pos[1], projectile_radius * 2.2, projectile_radius * 2.2))
        if projectile_pos[0] > WIDTH:
            collect_projectile = False
    
    if collect_projectile == False and collect_projectile_axis == 2:
        projectile_pos = (WIDTH,random.randint(0, HEIGHT))
        projectile_square = pg.draw.rect(screen, "black", pg.Rect(projectile_pos[0], projectile_pos[1], projectile_radius * 2.2, projectile_radius * 2.2))
        collect_projectile = True
    elif collect_projectile == True and collect_projectile_axis == 2:
        projectile_pos = (projectile_pos[0] - projectile_X_init_speed, projectile_pos[1])
        projectile_square = pg.draw.rect(screen, "black", pg.Rect(projectile_pos[0], projectile_pos[1], projectile_radius * 2.2, projectile_radius * 2.2))
        if projectile_pos[0] < 0:
            collect_projectile = False

    if collect_projectile == False and collect_projectile_axis == 3:
        projectile_pos = (random.randint(0, WIDTH),0)
        projectile_square = pg.draw.rect(screen, "black", pg.Rect(projectile_pos[0], projectile_pos[1], projectile_radius * 2.2, projectile_radius * 2.2))
        collect_projectile = True
    elif collect_projectile == True and collect_projectile_axis == 3:
        projectile_pos = (projectile_pos[0], projectile_pos[1]+projectile_Y_init_speed)
        projectile_square = pg.draw.rect(screen, "black", pg.Rect(projectile_pos[0], projectile_pos[1], projectile_radius * 2.2, projectile_radius * 2.2))
        if projectile_pos[1] > HEIGHT:
            collect_projectile = False

    if collect_projectile == False and collect_projectile_axis == 4:
        projectile_pos = (random.randint(0, WIDTH),HEIGHT)
        projectile_square = pg.draw.rect(screen, "black", pg.Rect(projectile_pos[0], projectile_pos[1], projectile_radius * 2.2, projectile_radius * 2.2))
        collect_projectile = True
    elif collect_projectile == True and collect_projectile_axis == 4:
        projectile_pos = (projectile_pos[0], projectile_pos[1]-projectile_Y_init_speed)
        projectile_square = pg.draw.rect(screen, "black", pg.Rect(projectile_pos[0], projectile_pos[1], projectile_radius * 2.2, projectile_radius * 2.2))
        if projectile_pos[1] < 0:
            collect_projectile = False
    
    return projectile_square

def generate_challenge_hazards():
    global projectile_left, projectile_right, projectile_top, projectile_bottom, projectile_left_pos, projectile_right_pos, projectile_top_pos, projectile_bottom_pos, projectile_radius, projectile_X_init_speed, projectile_Y_init_speed
    projectile_radius = 30 if DIFFICULTY_SETTING == "Medium" else 20 if DIFFICULTY_SETTING == "Easy" else 35
    projectile_X_init_speed = WIDTH/100 if DIFFICULTY_SETTING == "Medium" else WIDTH/150 if DIFFICULTY_SETTING == "Easy" else WIDTH/75
    projectile_Y_init_speed = HEIGHT/100 if DIFFICULTY_SETTING == "Medium" else HEIGHT/150 if DIFFICULTY_SETTING == "Easy" else HEIGHT/75
    circle_left = circle_right = circle_top = circle_bottom = None
    
    if projectile_left == False:
        projectile_left_pos = (0,player_pos.y)
        circle_left = pg.draw.circle(screen, "blue", projectile_left_pos, projectile_radius)
        projectile_left = True
    elif projectile_left == True:
        projectile_left_pos = (projectile_left_pos[0] + projectile_X_init_speed, projectile_left_pos[1])
        circle_left = pg.draw.circle(screen, "blue", projectile_left_pos, projectile_radius)
        if projectile_left_pos[0] > WIDTH:
            projectile_left = False

    if projectile_top == False and projectile_left_pos[0] >= WIDTH/4:
        projectile_top_pos = (player_pos.x,0)
        circle_top = pg.draw.circle(screen, "dark blue", projectile_top_pos, projectile_radius)
        projectile_top = True
    elif projectile_top == True:
        projectile_top_pos = (projectile_top_pos[0], projectile_top_pos[1]+projectile_Y_init_speed)
        circle_top = pg.draw.circle(screen, "dark blue", projectile_top_pos, projectile_radius)
        if projectile_top_pos[1] > HEIGHT:
            projectile_top = False

    if projectile_right == False and projectile_top_pos[1] >= WIDTH/4:
        projectile_right_pos = (WIDTH,player_pos.y)
        circle_right = pg.draw.circle(screen, "blue", projectile_right_pos, projectile_radius)
        projectile_right = True
    elif projectile_right == True:
        projectile_right_pos = (projectile_right_pos[0] - projectile_X_init_speed, projectile_right_pos[1])
        circle_right = pg.draw.circle(screen, "blue", projectile_right_pos, projectile_radius)
        if projectile_right_pos[0] < 0:
            projectile_right = False

    if projectile_bottom == False and projectile_right_pos[0] <= (WIDTH - WIDTH/4):
        projectile_bottom_pos = (player_pos.x,HEIGHT)
        circle_bottom = pg.draw.circle(screen, "dark blue", projectile_bottom_pos, projectile_radius)
        projectile_bottom = True
    elif projectile_bottom == True:
        projectile_bottom_pos = (projectile_bottom_pos[0], projectile_bottom_pos[1]-projectile_Y_init_speed)
        circle_bottom = pg.draw.circle(screen, "dark blue", projectile_bottom_pos, projectile_radius)
        if projectile_bottom_pos[1] < 0:
            projectile_bottom = False

    hazards = []
    for circle in [circle_left, circle_right, circle_top, circle_bottom]:
        if circle != None:
            hazards.append(circle)
    
    return hazards


def reset_game():
    global projectile_left, projectile_right, projectile_top, projectile_bottom, player_pos, score, player1_pos, player2_pos, player1_alive, player2_alive, collect_projectile, score_p1_collide, score_p2_collide, projectile_left_pos, projectile_right_pos, projectile_top_pos, projectile_bottom_pos
    projectile_left = projectile_right = projectile_top = projectile_bottom = False
    if NUM_PLAYERS == "1-Player":
        if GAMEMODE == "Collect":
            collect_projectile = False
        if GAMEMODE == "Challenge":
            projectile_left_pos = (0,0) 
            projectile_right_pos = (WIDTH,0) 
            projectile_top_pos = (0,0)
            projectile_bottom_pos = (0,HEIGHT)
        player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    else:
        if GAMEMODE == "Collect":
            collect_projectile = False
            if NUM_PLAYERS == "VS":
                score_p1_collide = 0
                score_p2_collide = 0
        if GAMEMODE == "Challenge":
            projectile_left_pos = (0,0) 
            projectile_right_pos = (WIDTH,0) 
            projectile_top_pos = (0,0)
            projectile_bottom_pos = (0,HEIGHT)
        player1_pos = pg.Vector2(WIDTH/3, HEIGHT/2)
        player2_pos = pg.Vector2(WIDTH/1.5, HEIGHT/2)
        player1_alive = True
        player2_alive = True
    score = 0

def classic_mode():
    global CLASSIC_OP_SCORES, CLASSIC_TP_SCORES, CLASSIC_VS_SCORES
    if NUM_PLAYERS == "1-Player":
        player = pg.draw.circle(screen, "red", player_pos, 40)
        handle_movement(player)

        # HAZARDS
        hazards = generate_hazards_classic()
        collide = player.collidelist(hazards)

        if not (collide == -1):
            CLASSIC_OP_SCORES.append(score)
            CLASSIC_OP_SCORES.sort()
            reset_game()
            game_over()
    else:
        global player1_alive, player2_alive
        player1 = None
        player2 = None
        if player1_alive:
            player1 = pg.draw.circle(screen, "red", player1_pos, 40)
        if player2_alive:
            player2 = pg.draw.circle(screen, "orange", player2_pos, 40)
        handle_movement(None, player1, player2)
        
        hazards = generate_hazards_classic()

        if player1_alive:
            collide_player1 = player1.collidelist(hazards)
        if player2_alive:
            collide_player2 = player2.collidelist(hazards)

        if NUM_PLAYERS == "2-Player":
            if player1_alive and collide_player1 != -1:
                player1_alive = False
            if player2_alive and collide_player2 != -1:
                player2_alive = False
            if not (player1_alive or player2_alive):
                CLASSIC_TP_SCORES.append(score)
                CLASSIC_TP_SCORES.sort()
                reset_game()
                game_over()
        elif NUM_PLAYERS == "VS":
            if collide_player1 != -1 and collide_player2 == -1:
                CLASSIC_VS_SCORES.append(score)
                CLASSIC_VS_SCORES.sort()
                player_win(2)
            if collide_player1 == -1 and collide_player2 != -1:
                CLASSIC_VS_SCORES.append(score)
                CLASSIC_VS_SCORES.sort()
                player_win(1)
            if collide_player1 != -1 and collide_player2 != -1:
                CLASSIC_VS_SCORES.append(score)
                CLASSIC_VS_SCORES.sort()
                player_win(-1)

def collect_mode(start_time):
    global score, projectile_left, projectile_right, projectile_top, projectile_bottom, COLLECT_OP_SCORES, COLLECT_TP_SCORES, COLLECT_VS_SCORES

    # Timer to the screen
    timer = font.render("{0}".format((30000 + start_time - pg.time.get_ticks())//1000), True, "black")
    timer_rect = timer.get_rect()
    screen.blit(timer, ((WIDTH-timer_rect.w)/2, 100))

    if NUM_PLAYERS == "1-Player":
        player = pg.draw.circle(screen, "red", player_pos, 40)
        handle_movement(player)

        # HAZARDS
        haz_l, haz_r, haz_t, haz_b = generate_hazards_classic()
        true_haz = generate_collect_mode_hazard()
        collide1 = player.colliderect(haz_l)
        collide2 = player.colliderect(haz_r)
        collide3 = player.colliderect(haz_t)
        collide4 = player.colliderect(haz_b)
        collide_haz = player.colliderect(true_haz)

        if collide1:
            score += 1
            projectile_left = False
        if collide2:
            score += 1
            projectile_right = False
        if collide3:
            score += 1
            projectile_top = False
        if collide4:
            score += 1
            projectile_bottom = False

        if 30 + (start_time - pg.time.get_ticks())//1000 == 0 or collide_haz:
            COLLECT_OP_SCORES.append(score)
            COLLECT_OP_SCORES.sort()
            reset_game()
            game_over()   
    else:
        global player1_alive, player2_alive
        player1 = None
        player2 = None
        if player1_alive:
            player1 = pg.draw.circle(screen, "red", player1_pos, 40)
        if player2_alive:
            player2 = pg.draw.circle(screen, "orange", player2_pos, 40)
        handle_movement(None, player1, player2)
        
        haz_l, haz_r, haz_t, haz_b = generate_hazards_classic()
        true_haz = generate_collect_mode_hazard()
        # Player 1 Collisions
        if player1_alive:
            collide1_p1 = player1.colliderect(haz_l)
            collide2_p1 = player1.colliderect(haz_r)
            collide3_p1 = player1.colliderect(haz_t)
            collide4_p1 = player1.colliderect(haz_b)
            collide_haz_p1 = player1.colliderect(true_haz)
        # Player 2 Collisions
        if player2_alive:
            collide1_p2 = player2.colliderect(haz_l)
            collide2_p2 = player2.colliderect(haz_r)
            collide3_p2 = player2.colliderect(haz_t)
            collide4_p2 = player2.colliderect(haz_b)
            collide_haz_p2 = player2.colliderect(true_haz)

        # Handle Death Collisions Depending on the Game Mode
        if NUM_PLAYERS == "2-Player":
            if player1_alive and collide1_p1 or player2_alive and collide1_p2:
                score += 1
                projectile_left = False
            if player1_alive and collide2_p1 or player2_alive and collide2_p2:
                score += 1
                projectile_right = False
            if player1_alive and collide3_p1 or player2_alive and collide3_p2:
                score += 1
                projectile_top = False
            if player1_alive and collide4_p1 or player2_alive and collide4_p2:
                score += 1
                projectile_bottom = False
            if player1_alive and collide_haz_p1 != 0:
                player1_alive = False
            if player2_alive and collide_haz_p2 != 0:
                player2_alive = False
            if not (player1_alive or player2_alive) or (30 + (start_time - pg.time.get_ticks())//1000 == 0):
                COLLECT_TP_SCORES.append(score)
                COLLECT_TP_SCORES.sort()
                reset_game()
                game_over()
        if NUM_PLAYERS == "VS":
            global score_p1_collide, score_p2_collide, collect_projectile
            penalty = 10 if DIFFICULTY_SETTING == "Medium" else 15 if DIFFICULTY_SETTING == "Hard" else 5
            if player1_alive and collide1_p1:
                score_p1_collide += 1
                projectile_left = False
            if player2_alive and collide1_p2:
                score_p2_collide += 1
                projectile_left = False
            if player1_alive and collide2_p1:
                score_p1_collide += 1
                projectile_right = False
            if player2_alive and collide2_p2:
                score_p2_collide += 1
                projectile_right = False
            if player1_alive and collide3_p1:
                score_p1_collide += 1
                projectile_top = False
            if player2_alive and collide3_p2:
                score_p2_collide += 1
                projectile_top = False
            if player1_alive and collide4_p1:
                score_p1_collide += 1
                projectile_bottom = False
            if player2_alive and collide4_p2:
                score_p2_collide += 1
                projectile_bottom = False

            if collide_haz_p1 != 0:
                score_p1_collide -= penalty
                collect_projectile = False
            if collide_haz_p2 != 0:
                score_p2_collide -= penalty
                collect_projectile = False
            if 30 + (start_time - pg.time.get_ticks())//1000 == 0:
                if score_p1_collide > score_p2_collide:
                    player_win(1)
                    COLLECT_VS_SCORES.append(score_p1_collide)
                    COLLECT_VS_SCORES.sort()
                if score_p1_collide < score_p2_collide:
                    player_win(2)
                    COLLECT_VS_SCORES.append(score_p2_collide)
                    COLLECT_VS_SCORES.sort()
                else:
                    COLLECT_VS_SCORES.append(score_p1_collide)
                    COLLECT_VS_SCORES.sort()
                    player_win(-1)

def challenge_mode():
    global CHALLENGE_OP_SCORES, CHALLENGE_TP_SCORES, CHALLENGE_VS_SCORES
    if NUM_PLAYERS == "1-Player":
        player = pg.draw.circle(screen, "red", player_pos, 40)
        handle_movement(player)

        hazards = generate_challenge_hazards()
        collide = player.collidelist(hazards)

        if not (collide == -1):
            CHALLENGE_OP_SCORES.append(score)
            CHALLENGE_OP_SCORES.sort()
            reset_game()
            game_over()
    else:
        global player1_alive, player2_alive
        player1 = None
        player2 = None
        if player1_alive:
            player1 = pg.draw.circle(screen, "red", player1_pos, 40)
        if player2_alive:
            player2 = pg.draw.circle(screen, "orange", player2_pos, 40)
        handle_movement(None, player1, player2)
        
        hazards = generate_hazards_classic()

        if player1_alive:
            collide_player1 = player1.collidelist(hazards)
        if player2_alive:
            collide_player2 = player2.collidelist(hazards)

        if NUM_PLAYERS == "2-Player":
            if player1_alive and collide_player1 != -1:
                player1_alive = False
            if player2_alive and collide_player2 != -1:
                player2_alive = False
            if not (player1_alive or player2_alive):
                CHALLENGE_TP_SCORES.append(score)
                CHALLENGE_TP_SCORES.sort()
                reset_game()
                game_over()
        elif NUM_PLAYERS == "VS":
            if collide_player1 != -1 and collide_player2 == -1:
                CHALLENGE_VS_SCORES.append(score)
                CHALLENGE_VS_SCORES.sort()
                player_win(2)
            if collide_player1 == -1 and collide_player2 != -1:
                CHALLENGE_VS_SCORES.append(score)
                CHALLENGE_VS_SCORES.sort()
                player_win(1)
            if collide_player1 != -1 and collide_player2 != -1:
                CHALLENGE_VS_SCORES.append(score)
                CHALLENGE_VS_SCORES.sort()
                player_win(-1)

###################################################################################################################
# GAME LOOP
###################################################################################################################

def play():
    start_time = pg.time.get_ticks()
    global score, score_p1_collide, score_p2_collide
    pg.display.set_caption("Play Game")
    while True:
        if GAMEMODE == "Classic" or GAMEMODE == "Challenge":
            score = (pg.time.get_ticks() - start_time) // 1000
        
        for event in pg.event.get():
            check_exit(event)

        screen.fill("grey")

        if GAMEMODE == "Classic":
            classic_mode()
        if GAMEMODE == "Collect":
            collect_mode(start_time)
        if GAMEMODE == "Challenge":
            challenge_mode()
            
        # Handle scores for collect vs mode
        if GAMEMODE == "Collect" and NUM_PLAYERS == "VS":
            player1_txt = font.render("Player 1:", True, "black")
            player2_txt = font.render("Player 2:", True, "black")
            score1 = font.render("{0}".format(score_p1_collide), True, "black")
            score2 = font.render("{0}".format(score_p2_collide), True, "black")
            player1_txt_rect = player1_txt.get_rect()
            player2_txt_rect = player2_txt.get_rect()
            screen.blit(player1_txt, ((WIDTH - player1_txt_rect.w)/4, 60))
            screen.blit(player2_txt, ((WIDTH - player2_txt_rect.w)/1.25, 60))
            screen.blit(score1, ((WIDTH/4)+10, 100))
            screen.blit(score2, ((WIDTH/1.25)-10, 100))
        else:
            text = font.render("Score {0}".format(score), True, "black")
            text_rect = text.get_rect()
            screen.blit(text, ((WIDTH - text_rect.w)/2,20))

        # Display work on screen
        pg.display.flip()     
        clock.tick(60)
 
def settings(return_menu_type):
    global MUTED, DIFFICULTY_SETTING, NUM_PLAYERS, GAMEMODE
    pg.display.set_caption("Settings")
    while True:
        screen.fill("grey")
        MOUSE_POS = pg.mouse.get_pos()
        header = header_font.render("Settings", True, "black")
        header_rect = header.get_rect()
        screen.blit(header, ((WIDTH-header_rect.w)/2,(HEIGHT-header_rect.h)/8))

        PLAYER_NUM_BTN = Button(image=pg.image.load("assets/Btn-Rect2.png"), pos=(WIDTH/2, HEIGHT/1.25 - 320), text_input="1-PLAYER", font=font, base_color="grey", hovering_color="white")
        DIFFICULTY_BTN = Button(image=pg.image.load("assets/Btn-Rect2.png"), pos=(WIDTH/2, HEIGHT/1.25 - 240), text_input="MEDIUM", font=font, base_color="grey", hovering_color="white")
        GAMEMODE_BTN = Button(image=pg.image.load("assets/Btn-Rect2.png"), pos=(WIDTH/2, HEIGHT/1.25 - 160), text_input="GAMEMODE", font=font, base_color="grey", hovering_color="white")
        MUTE_BTN = Button(image=pg.image.load("assets/Btn-Rect2.png"), pos=(WIDTH/2, HEIGHT/1.25 - 80), text_input="MUTE", font=font, base_color="grey", hovering_color="white")
        RETURN_BTN = Button(image=pg.image.load("assets/Btn-Rect2.png"), pos=(WIDTH/2, HEIGHT/1.25), text_input="RETURN", font=font, base_color="grey", hovering_color="white")


        for btn in [RETURN_BTN, DIFFICULTY_BTN, MUTE_BTN, PLAYER_NUM_BTN, GAMEMODE_BTN]:
            if btn == MUTE_BTN:
                if MUTED == True:
                    MUTE_BTN.update_text("UNMUTE")
                else:
                    MUTE_BTN.update_text("MUTE")
            elif btn == DIFFICULTY_BTN:
                if DIFFICULTY_SETTING == "Hard":
                    DIFFICULTY_BTN.update_text("HARD")
                elif DIFFICULTY_SETTING == "Easy":
                    DIFFICULTY_BTN.update_text("EASY")
                else:
                    DIFFICULTY_BTN.update_text("MEDIUM")
            elif btn == PLAYER_NUM_BTN:
                if NUM_PLAYERS == "2-Player":
                    PLAYER_NUM_BTN.update_text("2-PLAYER")
                if NUM_PLAYERS == "VS":
                    PLAYER_NUM_BTN.update_text("1 VS 2")
                if NUM_PLAYERS == "1-Player":
                    PLAYER_NUM_BTN.update_text("1-PLAYER")
            elif btn == GAMEMODE_BTN:
                if GAMEMODE == "Classic":
                    GAMEMODE_BTN.update_text("CLASSIC")
                elif GAMEMODE == "Collect":
                    GAMEMODE_BTN.update_text("COLLECT")
                else:
                    GAMEMODE_BTN.update_text("CHALLENGE")
            btn.changeColor(MOUSE_POS)
            btn.update(screen)

        for event in pg.event.get():
            check_exit(event)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE or event.key == pg.K_RETURN:
                    menu_screen(return_menu_type)
            elif event.type == pg.MOUSEBUTTONDOWN:
                if RETURN_BTN.checkForInput(MOUSE_POS):
                    menu_screen(return_menu_type)
                if PLAYER_NUM_BTN.checkForInput(MOUSE_POS):
                    if NUM_PLAYERS == "1-Player":
                        NUM_PLAYERS = "2-Player"
                    elif NUM_PLAYERS == "2-Player":
                        NUM_PLAYERS = "VS"
                    else:
                        NUM_PLAYERS = "1-Player"
                if DIFFICULTY_BTN.checkForInput(MOUSE_POS):
                    if DIFFICULTY_SETTING == "Medium":
                        DIFFICULTY_SETTING = "Hard"
                    elif DIFFICULTY_SETTING == "Hard":
                        DIFFICULTY_SETTING = "Easy"
                    else:
                        DIFFICULTY_SETTING = "Medium"
                if MUTE_BTN.checkForInput(MOUSE_POS):
                    if MUTED == False:
                        MUTED = True
                    else:
                        MUTED = False
                if GAMEMODE_BTN.checkForInput(MOUSE_POS):
                    if GAMEMODE == "Classic":
                        GAMEMODE = "Collect"
                    elif GAMEMODE == "Collect":
                        GAMEMODE = "Challenge"
                    else:
                        GAMEMODE = "Classic"

        pg.display.flip()

def player_win(player_num):
    pg.display.set_caption("Win Screen")
    while True:
        MOUSE_POS = pg.mouse.get_pos()
        reset_game()
        screen.fill("grey")
        if player_num != -1:
            header = header_font.render("Player {} Wins!".format(player_num), True, "black")
            img = pg.image.load("assets/trophy.png")
            img = pg.transform.scale(img, (img.get_width()/3, img.get_height()/3))
        else:
            header = header_font.render("Tie Game, Play Again!", True, "black")
            img = pg.image.load("assets/tie.png")
        header_rect = header.get_rect()
        img_rect = img.get_rect()
        screen.blit(header, ((WIDTH-header_rect.w)/2,(HEIGHT-header_rect.h)/8))
        screen.blit(img, ((WIDTH-img_rect.w)/2, HEIGHT/4.5))

        PLAY_AGAIN_BTN = Button(image=pg.image.load("assets/Btn-Rect2.png"), pos=(WIDTH/2 - 160, HEIGHT/1.2), text_input="PLAY AGAIN", font=font, base_color="grey", hovering_color="white")
        MENU_BTN = Button(image=pg.image.load("assets/Btn-Rect2.png"), pos=(WIDTH/2 + 160, HEIGHT/1.2), text_input="MAIN MENU", font=font, base_color="grey", hovering_color="white")

        for btn in [PLAY_AGAIN_BTN, MENU_BTN]:
            btn.changeColor(MOUSE_POS)
            btn.update(screen)

        for event in pg.event.get():
            check_exit(event)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    play()
                if event.key == pg.K_ESCAPE:
                    main_menu()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_AGAIN_BTN.checkForInput(MOUSE_POS):
                    play()
                if MENU_BTN.checkForInput(MOUSE_POS):
                    main_menu()

        pg.display.flip()

def scores(return_menu_type):
    pg.display.set_caption("Scores")
    global SCORES
    while True:
        screen.fill("grey")
        MOUSE_POS = pg.mouse.get_pos()
        
        RETURN_BTN = Button(image=pg.image.load("assets/Btn-Rect2.png"), pos=(WIDTH/2, HEIGHT/1.2), text_input="RETURN", font=font, base_color="grey", hovering_color="white")
        RETURN_BTN.changeColor(MOUSE_POS)
        RETURN_BTN.update(screen)

        if GAMEMODE == "Classic":
            if NUM_PLAYERS == "1-Player":
                SCORES = CLASSIC_OP_SCORES[:]
                title = "CLASSIC 1-PLAYER SCORES:"
            elif NUM_PLAYERS == "2-Player":
                SCORES = CLASSIC_TP_SCORES[:]
                title = "CLASSIC 2-PLAYER SCORES:"
            else:
                SCORES = CLASSIC_VS_SCORES[:]
                title = "CLASSIC VS SCORES:"
        elif GAMEMODE == "Collect":
            if NUM_PLAYERS == "1-Player":
                SCORES = COLLECT_OP_SCORES[:]
                title = "COLLECT 1-PLAYER SCORES:"
            elif NUM_PLAYERS == "2-Player":
                SCORES = COLLECT_TP_SCORES[:]
                title = "COLLECT 2-PLAYER SCORES:"
            else:
                SCORES = COLLECT_VS_SCORES[:]
                title = "COLLECT VS SCORES:"
        else:
            if NUM_PLAYERS == "1-Player":
                SCORES = CHALLENGE_OP_SCORES[:]  
                title = "CHALLENGE 1-PLAYER SCORES:"
            elif NUM_PLAYERS == "2-Player":
                SCORES = CHALLENGE_TP_SCORES[:]
                title = "CHALLENGE 2-PLAYER SCORES:"
            else:
                SCORES = CHALLENGE_VS_SCORES[:]  
                title = "CHALLENGE VS SCORES:"  

        header = header_font.render(title, True, "black")
        header_rect = header.get_rect()
        screen.blit(header, ((WIDTH-header_rect.w)/2,(HEIGHT-header_rect.h)/8)) 

        score1 = font.render("1. {0}".format(SCORES[len(SCORES)-1]), True, "black")
        score2 = font.render("2. {0}".format(SCORES[len(SCORES)-2]), True, "black")
        score3 = font.render("3. {0}".format(SCORES[len(SCORES)-3]), True, "black")
        score4 = font.render("4. {0}".format(SCORES[len(SCORES)-4]), True, "black")
        score5 = font.render("5. {0}".format(SCORES[len(SCORES)-5]), True, "black")

        y_pos = HEIGHT/3.5
        for s in [score1, score2, score3, score4, score5]:
            s_rect = s.get_rect()
            screen.blit(s, ((WIDTH-s_rect.w)/2, y_pos))
            y_pos += 70

        for event in pg.event.get():
            check_exit(event)
            if event.type == pg.MOUSEBUTTONDOWN:
                if RETURN_BTN.checkForInput(MOUSE_POS):
                    menu_screen(return_menu_type)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    menu_screen(return_menu_type)

        pg.display.flip()

def menu_screen(menu_type):
    play_or_restart = "PLAY" if menu_type == "Main Menu" else "RESTART"
    pg.display.set_caption(menu_type)
    while True:
        screen.fill("grey")
        MOUSE_POS = pg.mouse.get_pos()
        header = header_font.render(menu_type, True, "black")
        header_rect = header.get_rect()
        screen.blit(header, ((WIDTH-header_rect.w)/2, (HEIGHT-header_rect.h)/5))

        PLAY_BTN = Button(image=pg.image.load("assets/Btn-Rect2.png"), pos=(WIDTH/2, HEIGHT/2 - 80), text_input=play_or_restart, font=font, base_color="grey", hovering_color="white")
        SCORES_BTN = Button(image=pg.image.load("assets/Btn-Rect2.png"), pos=(WIDTH/2, HEIGHT/2), text_input="SCORES", font=font, base_color="grey", hovering_color="white")        
        SETTINGS_BTN = Button(image=pg.image.load("assets/Btn-Rect2.png"), pos=(WIDTH/2, HEIGHT/2 + 80), text_input="SETTINGS", font=font, base_color="grey", hovering_color="white")
        QUIT_BTN = Button(image=pg.image.load("assets/Btn-Rect2.png"), pos=(WIDTH/2, HEIGHT/2 + 160), text_input="QUIT", font=font, base_color="grey", hovering_color="white")

        for button in [PLAY_BTN, SETTINGS_BTN, SCORES_BTN, QUIT_BTN]:
            button.changeColor(MOUSE_POS)
            button.update(screen)

        for event in pg.event.get():
            check_exit_pygame_menu(event)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    play()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BTN.checkForInput(MOUSE_POS):
                    play()
                if SETTINGS_BTN.checkForInput(MOUSE_POS):
                    settings(menu_type)
                if SCORES_BTN.checkForInput(MOUSE_POS):
                    scores(menu_type)
                if QUIT_BTN.checkForInput(MOUSE_POS):
                    pg.quit()
                    sys.exit()

        pg.display.flip()

def game_over():
    menu_screen("Game Over")

def main_menu():
    menu_screen("Main Menu")

main_menu()
import random, pygame as pg, sys
from button import Button

pg.init()

SIZE = (WIDTH, HEIGHT) = (1280, 720)
screen = pg.display.set_mode(SIZE)
clock = pg.time.Clock()     #set the clock to the pygame clock
CURRENT_SCREEN = "Main Menu"

# Projectiles initial settings
projectile_left = projectile_right = projectile_top = projectile_bottom = False
projectile_radius = 30
projectile_X_init_speed = WIDTH/100
projectile_Y_init_speed = HEIGHT/100

player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

score = -2
SCORES = [0,0,0,0,0]
MUTED = False
DIFFICULTY_SETTING = "Medium"
GAMEMODE = "Classic"

# For 2 player mode
NUM_PLAYERS = "1-Player"
player1_pos = pg.Vector2(WIDTH/3, HEIGHT/2)
player2_pos = pg.Vector2(WIDTH/1.5, HEIGHT/2)
player1_alive = True
player2_alive = True

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

def generate_hazards():
    global score, projectile_left, projectile_right, projectile_top, projectile_bottom, projectile_left_pos, projectile_right_pos, projectile_top_pos, projectile_bottom_pos, projectile_radius, projectile_X_init_speed, projectile_Y_init_speed
    projectile_radius = 30 if DIFFICULTY_SETTING == "Medium" else 20 if DIFFICULTY_SETTING == "Easy" else 35
    projectile_X_init_speed = WIDTH/100 if DIFFICULTY_SETTING == "Medium" else WIDTH/150 if DIFFICULTY_SETTING == "Easy" else WIDTH/75
    projectile_Y_init_speed = HEIGHT/100 if DIFFICULTY_SETTING == "Medium" else HEIGHT/150 if DIFFICULTY_SETTING == "Easy" else HEIGHT/75
    if projectile_left == False:
        score += 1
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
        score += 1
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

def reset_game():
    global projectile_left, projectile_right, projectile_top, projectile_bottom, player_pos, score, player1_pos, player2_pos, player1_alive, player2_alive
    projectile_left = projectile_right = projectile_top = projectile_bottom = False
    if NUM_PLAYERS == "1-Player":
        player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    else:
        player1_pos = pg.Vector2(WIDTH/3, HEIGHT/2)
        player2_pos = pg.Vector2(WIDTH/1.5, HEIGHT/2)
        player1_alive = True
        player2_alive = True
    score = -2

###################################################################################################################
# GAME LOOP
###################################################################################################################

def play():
    pg.display.set_caption("Play Game")
    while True:
        for event in pg.event.get():
            check_exit(event)

        screen.fill("grey")

        if NUM_PLAYERS == "1-Player":
            player = pg.draw.circle(screen, "red", player_pos, 40)
            handle_movement(player)

            # HAZARDS
            hazards = generate_hazards()
            collide = player.collidelist(hazards)

            if not (collide == -1):
                SCORES.append(score)
                SCORES.sort()
                reset_game()
                game_over()
        else:
            global player1_alive, player2_alive
            if player1_alive:
                player1 = pg.draw.circle(screen, "red", player1_pos, 40)
            if player2_alive:
                player2 = pg.draw.circle(screen, "orange", player2_pos, 40)
            handle_movement(None, player1, player2)
            
            hazards = generate_hazards()
            collide_player1 = player1.collidelist(hazards)
            collide_player2 = player2.collidelist(hazards)

            if NUM_PLAYERS == "2-Player":
                if collide_player1 != -1:
                    player1_alive = False
                if collide_player2 != -1:
                    player2_alive = False
                if player1_alive == False and player2_alive == False:
                    SCORES.append(score)
                    SCORES.sort()
                    reset_game()
                    game_over()
            else:
                if collide_player1 != -1 and collide_player2 == -1:
                    player_win(2)
                if collide_player1 == -1 and collide_player2 != -1:
                    player_win(1)
                if collide_player1 != -1 and collide_player2 != -1:
                    player_win(-1)
        # Handle scores
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
                elif NUM_PLAYERS == "Versus":
                    PLAYER_NUM_BTN.update_text("1 VS 2")
                else:
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
                        NUM_PLAYERS = "Versus"
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
    while True:
        screen.fill("grey")
        MOUSE_POS = pg.mouse.get_pos()
        header = header_font.render("Scores", True, "black")
        header_rect = header.get_rect()
        screen.blit(header, ((WIDTH-header_rect.w)/2,(HEIGHT-header_rect.h)/8))

        RETURN_BTN = Button(image=pg.image.load("assets/Btn-Rect2.png"), pos=(WIDTH/2, HEIGHT/1.2), text_input="RETURN", font=font, base_color="grey", hovering_color="white")

        RETURN_BTN.changeColor(MOUSE_POS)
        RETURN_BTN.update(screen)

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
        SETTINGS_BTN = Button(image=pg.image.load("assets/Btn-Rect2.png"), pos=(WIDTH/2, HEIGHT/2), text_input="SETTINGS", font=font, base_color="grey", hovering_color="white")
        SCORES_BTN = Button(image=pg.image.load("assets/Btn-Rect2.png"), pos=(WIDTH/2, HEIGHT/2 + 80), text_input="SCORES", font=font, base_color="grey", hovering_color="white")
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
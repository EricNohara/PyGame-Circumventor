import random, pygame as pg, sys
from button import Button

pg.init()

SIZE = (WIDTH, HEIGHT) = (1280, 720)
screen = pg.display.set_mode(SIZE)
clock = pg.time.Clock()     #set the clock to the pygame clock
CURRENT_SCREEN = "Main Menu"

projectile_left = projectile_right = projectile_top = projectile_bottom = False
projectile_radius = 30
player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)
score = 0

font = pg.font.Font('freesansbold.ttf', 30)
header_font = pg.font.Font('freesansbold.ttf', 60)

###################################################################################################################
# HELPER FUNCTIONS
###################################################################################################################

def check_exit_pygame(event):
    if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
    elif event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
            pg.quit()
            sys.exit()
            
def handle_movement(player):
    keys = pg.key.get_pressed()
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

def generate_hazards():
    global score, projectile_left, projectile_right, projectile_top, projectile_bottom, projectile_left_pos, projectile_right_pos, projectile_top_pos, projectile_bottom_pos
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
    
    return [circle_left, circle_right, circle_top, circle_bottom]

def reset_game():
    global projectile_left, projectile_right, projectile_top, projectile_bottom, player_pos, score
    projectile_left = projectile_right = projectile_top = projectile_bottom = False
    player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    score = 0

###################################################################################################################
# GAME LOOP
###################################################################################################################

def play():
    pg.display.set_caption("Play Game")
    while True:
        for event in pg.event.get():
            check_exit_pygame(event)

        screen.fill("grey")

        player = pg.draw.circle(screen, "red", player_pos, 40)

        handle_movement(player)

        # HAZARDS
        hazards = generate_hazards()

        collide = player.collidelist(hazards)

        if not (collide == -1):
            reset_game()
            game_over()

        text = font.render("Score {0}".format(score), True, "black")
        text_rect = text.get_rect()
        screen.blit(text, ((WIDTH - text_rect.w)/2,20))
        
        # Display work on screen
        pg.display.flip()     
        clock.tick(60)
 
def settings():
    pass

def scores():
    pass

def menu_screen(type):
    play_or_restart = "PLAY" if type == "Main Menu" else "RESTART"
    pg.display.set_caption(type)
    while True:
        screen.fill("grey")
        MOUSE_POS = pg.mouse.get_pos()
        header = header_font.render(type, True, "black")
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
            check_exit_pygame(event)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    play()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BTN.checkForInput(MOUSE_POS):
                    play()
                if SETTINGS_BTN.checkForInput(MOUSE_POS):
                    settings()
                if SCORES_BTN.checkForInput(MOUSE_POS):
                    scores()
                if QUIT_BTN.checkForInput(MOUSE_POS):
                    pg.quit()
                    sys.exit()

        pg.display.flip()

def game_over():
    menu_screen("Game Over")

def main_menu():
    menu_screen("Main Menu")

main_menu()
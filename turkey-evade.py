import sys
import pygame as pg
import random

pg.init()

####################################################################################################################
# VARIABLES
####################################################################################################################
SIZE = WIDTH, HEIGHT = 1280, 720

screen = pg.display.set_mode(SIZE)      # set the screen
font = pg.font.Font('freesansbold.ttf', 30)
clock = pg.time.Clock()


# Colors
black = (0,0,0)
red = (255,0,0)
white = (255,255,255)

####################################################################################################################
# CLASSES
####################################################################################################################

class Player(object):
    def __init__(self):
        self.image = pg.image.load("assets/turkey.gif")
        self.rect = self.image.get_rect(center=(WIDTH/2, HEIGHT/2))

    def draw(self):
        screen.fill(black)
        screen.blit(self.image, self.rect)
   
    def handle_keys(self):
        keys = pg.key.get_pressed()
        move = 10 if keys[pg.K_LSHIFT] else 5
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.rect.y -= move
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.rect.y += move
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rect.x -= move
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rect.x += move

        

####################################################################################################################
# GAME LOOP
####################################################################################################################

def play():
    pg.display.set_caption("Play")
    screen.fill(black)

    player = Player()
    # bullet = Bullet()

    player.draw()

    # Gameplay loop
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        clock.tick(60)      #60 FPS game
        player.handle_keys()
        player.draw()
        pg.display.flip()

play()

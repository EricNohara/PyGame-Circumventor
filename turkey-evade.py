import sys
import pygame as pg
import random

pg.init()
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

    def update(self, direction):
        self.rect.x += direction[0] * 300 * DT
        self.rect.y += direction[1] * 300 * DT
        self.draw()
    
    def handle_keys(self):
        for event in pg.event.get():
            keys = pg.key.get_pressed()
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if keys[pg.K_UP] or keys[pg.K_w]:
                    self.update(UP)
                elif keys[pg.K_DOWN] or keys[pg.K_s]:
                    self.update(DOWN)
                elif keys[pg.K_LEFT] or keys[pg.K_a]:
                    self.update(LEFT)
                elif keys[pg.K_RIGHT] or keys[pg.K_d]:
                    self.update(RIGHT)
                elif keys[pg.K_ESCAPE]:
                    pg.quit()
                    sys.exit()

####################################################################################################################
# VARIABLES
####################################################################################################################
SIZE = WIDTH, HEIGHT = 1280, 720
UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)
DT = 0.05

screen = pg.display.set_mode(SIZE)      # set the screen
font = pg.font.Font('freesansbold.ttf', 30)
clock = pg.time.Clock()


# Colors
black = (0,0,0)
red = (255,0,0)
white = (255,255,255)

####################################################################################################################
# GAME LOOP
####################################################################################################################

def play():
    pg.display.set_caption("Play")
    # surface = pg.Surface(screen.get_size()).convert()     #create surface to draw on
    screen.fill(black)

    player = Player()
    # bullet = Bullet()

    screen.blit(player.image, player.rect)

    # Gameplay loop
    while True:
        clock.tick(60)      #60 FPS game
        # player.draw()
        player.handle_keys()

        pg.display.update()

play()

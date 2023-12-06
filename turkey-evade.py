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
        screen.blit(self.image, self.rect)
        pg.display.flip()

    def check_boundary(self):
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > (HEIGHT - self.rect.h):
            self.rect.y = HEIGHT - self.rect.h
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > (WIDTH - self.rect.w):
            self.rect.x = WIDTH - self.rect.w
   
    def handle_keys(self):
        keys = pg.key.get_pressed()
        move = 12 if keys[pg.K_LSHIFT] else 6
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.rect.y -= move
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.rect.y += move
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rect.x -= move
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rect.x += move
        self.check_boundary()
        
class Bullet(object):
    def __init__(self):
        self.image = pg.transform.rotozoom(pg.image.load("assets/bullet.png"), 0.15, 0.15)
        self.rect = self.image.get_rect()
        self.speed = (0,0)
        
    def draw(self):
        screen.blit(self.image, self.rect)
        # pg.display.flip()

    # def move_bullet(self):    
    #     while (self.rect.x >= 0 and self.rect.x <= WIDTH - self.rect.w) and (self.rect.y >= 0 and self.rect.y <= HEIGHT - self.rect.h):
    #         self.rect.x += self.speed[0]
    #         self.rect.y += self.speed[1]
    #         self.draw()

    def update_bullet_pos(self):
        if (self.rect.x >= 0 and self.rect.x <= WIDTH - self.rect.w) and (self.rect.y >= 0 and self.rect.y <= HEIGHT - self.rect.h):
            self.rect.x += self.speed[0]
            self.rect.y += self.speed[1]
        else:
            del self

    def spawn_bullet(self):
        spawn_edge = random.randint(0, 3)
        match spawn_edge:
            case 0:             # Edge 0: the top edge
                self.rect.y = 0
                self.rect.x = random.randint(0, WIDTH - self.rect.w)
                self.speed = (0, 1)
            case 1:             # Edge 1: the right edge
                self.rect.y = random.randint(0, HEIGHT - self.rect.h)
                self.rect.x = WIDTH - self.rect.w
                self.speed = (-1, 0)
            case 2:             # Edge 2: the bottom edge
                self.rect.y = HEIGHT - self.rect.h
                self.rect.x = random.randint(0, WIDTH - self.rect.w)
                self.speed = (0, -1)    
            case 3:             # Edge 3: the left edge
                self.rect.y = random.randint(0, HEIGHT-self.rect.h)
                self.rect.x = 0
                self.speed = (1, 0)
        self.draw()

####################################################################################################################
# HELPER FUNCTIONS
####################################################################################################################

# def draw_objects(objs):
#     for obj in objs:


####################################################################################################################
# GAME LOOP
####################################################################################################################

def play():
    pg.display.set_caption("Play")
    screen.fill(black)

    player = Player()
    bullet = Bullet()

    player.draw()

    # Gameplay loop
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        bullet.spawn_bullet()
        bullet.update_bullet_pos()
        bullet.draw()
        

        clock.tick(60)      #60 FPS game
        player.handle_keys()
        player.draw()
        screen.fill(black)
        pg.display.flip()

play()

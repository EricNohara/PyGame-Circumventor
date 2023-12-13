import pygame as pg
from pygame import mixer

pg.init()

# SCREEN SETTINGS
SIZE = (WIDTH, HEIGHT) = (1280, 720)
screen = pg.display.set_mode(SIZE)
clock = pg.time.Clock()     #set the clock to the pygame clock

# FONTS
font = pg.font.Font('freesansbold.ttf', 30)
header_font = pg.font.Font('freesansbold.ttf', 60)

# SOUNDS
def play_music():
    pg.mixer.music.load("assets/background.mp3")
    pg.mixer.music.play(-1)

def stop_music():
    pg.mixer.music.stop()

click_sound = pg.mixer.Sound("assets/click.mp3")
collect_sound = pg.mixer.Sound("assets/collect.mp3")
game_over_sound = pg.mixer.Sound("assets/game-over.mp3")
tie_sound = pg.mixer.Sound("assets/tie.mp3")
win_sound = pg.mixer.Sound("assets/win.mp3")
player_death = pg.mixer.Sound("assets/player-death.mp3")
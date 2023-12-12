import pygame as pg

pg.init()

# SCREEN SETTINGS
SIZE = (WIDTH, HEIGHT) = (1280, 720)
screen = pg.display.set_mode(SIZE)
clock = pg.time.Clock()     #set the clock to the pygame clock

# FONTS
font = pg.font.Font('freesansbold.ttf', 30)
header_font = pg.font.Font('freesansbold.ttf', 60)
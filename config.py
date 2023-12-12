import pygame as pg
from myconstants import *

pg.init()

# PROJECTILE INITIAL SETTINGS
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

# SCORE STATE VARIABLES
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
CURRENT_SCREEN = "Main Menu"

# PLAYER STATES
player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2) 
player1_pos = pg.Vector2(WIDTH/3, HEIGHT/2)
player2_pos = pg.Vector2(WIDTH/1.5, HEIGHT/2)
player1_alive = player2_alive = True
score_p1_collide = score_p2_collide = 0
import pygame as pg
import sys

def check_exit(event):
    if event.type == pg.QUIT:
        pg.quit()
        sys.exit()

def check_exit_pygame_menu(event):
    if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
    elif event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
            pg.quit()
            sys.exit() 
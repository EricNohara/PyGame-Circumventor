import pygame

pygame.init()
size = height, width = 1280, 720
screen = pygame.display.set_mode(size)
running = True
clock = pygame.time.Clock()
player = pygame.image.load('player.gif').convert()
background = pygame.image.load('background.png').convert()
screen.blit(background, (0,0))


while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

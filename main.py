import pygame
import random
import time

WIDTH = 1000
HEIGHT = 700
FPS = 144

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Танки 2D")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 30) 
font1 = pygame.font.Font(None, 20)
running = True

while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(font.render(str(round(clock.get_fps())), True, (255, 255, 150)), (10, 10))
    screen.blit(font1.render(str("FPS"), True, (255, 255, 150)), (50, 10))
    clock.tick(FPS)
    pygame.display.flip()
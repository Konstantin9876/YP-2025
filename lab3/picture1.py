import pygame
from pygame.draw import *

clock = pygame.time.Clock()
clock.tick(30)

screen = pygame.display.set_mode((800, 600))
screen.fill((255,255,255))

circle(screen, (255,255,0),(400,300),150)


circle(screen, (0,0,0),(330,230),31)
circle(screen, (0,0,0),(470,230),21)

circle(screen, (255,0,0),(330,230),30)
circle(screen, (255,0,0),(470,230),20)

circle(screen, (0,0,0),(330,230),10)
circle(screen, (0,0,0),(470,230),7.5)


pygame.draw.line(screen, (0, 0, 0), (370, 230), (280,120), 12)
pygame.draw.line(screen, (0, 0, 0), (440,230), (550,120), 12)

pygame.draw.line(screen, (0, 0, 0), (330, 380), (470,380), 20)





pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

import pygame
from pygame.draw import *

clock = pygame.time.Clock()
clock.tick(30)

screen = pygame.display.set_mode((800, 600))
screen.fill((255,255,255))



rect(screen, (179,179,179), (0,0, 800,300))

#Юрта
circle(screen, (0,0,0), (150,330), 100,5)
rect(screen, (255,255,255), (0,350, 800,300))


line(screen, (158, 158, 158), (50, 351), (248, 351), 2)
line(screen, (158, 158, 158), (50, 321), (248, 321), 2)
line(screen, (158, 158, 158), (55, 290), (243, 290), 2)
line(screen, (158, 158, 158), (75, 260), (223, 260), 2)


line(screen, (158, 158, 158), (75, 351), (75, 321), 2)
line(screen, (158, 158, 158), (150, 351), (150, 321), 2)
line(screen, (158, 158, 158), (225, 351), (225, 321), 2)

line(screen, (158, 158, 158), (105, 321), (105, 290), 2)
line(screen, (158, 158, 158), (180, 321), (180, 290), 2)

line(screen, (158, 158, 158), (95, 290), (95, 260), 2)
line(screen, (158, 158, 158), (160, 290), (160, 260), 2)
line(screen, (158, 158, 158), (210, 290), (210, 260), 2)

line(screen, (158, 158, 158), (105, 260), (105, 247), 2)
line(screen, (158, 158, 158), (180, 260), (180, 240), 2)

#Человек
ellipse(screen, (108,43,43), (530,375,120,150))
rect(screen, (255,255,255), (530,450, 200,100))


ellipse(screen, (179,179,179), (550,350,80,50))
ellipse(screen, (108,43,43), (560,357,60,37))

circle(screen, (108,43,43), (565,460), 15)
circle(screen, (108,43,43), (615,460), 15)

ellipse(screen, (108,43,43), (540,465,30,10))
ellipse(screen, (108,43,43), (610,465,30,10))

rect(screen, (68,25,25), (575,400, 30,50))
rect(screen, (68,25,25), (530,450, 120,10))

ellipse(screen, (108,43,43), (500,400,60,20))
ellipse(screen, (108,43,43), (615,400,60,20))

line(screen, (0, 0, 0), (500, 475), (500, 350), 2)

line(screen, (0, 0, 0), (580, 370), (575, 365), 2)
line(screen, (0, 0, 0), (600, 370), (605, 365), 2)
line(screen, (0, 0, 0), (580, 380), (610, 380), 2)


#Кошка
ellipse(screen, (179,179,179), (100,450,100,30))
circle(screen, (179,179,179), (120,442), 15)
circle(screen, (255,255,255), (114,440), 2)
circle(screen, (255,255,255), (128,440), 2)


ellipse(screen, (179,179,179), (100,465,10,50))
ellipse(screen, (179,179,179), (115,460,10,50))
ellipse(screen, (179,179,179), (175,465,10,50))
ellipse(screen, (179,179,179), (190,460,10,50))
ellipse(screen, (179,179,179), (190,410,10,50))


pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
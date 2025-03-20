import pygame
from pygame.draw import *

pygame.init()

clock = pygame.time.Clock()
clock.tick(30)

screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

# Функция для отрисовки юрты
def draw_yurt(x, y):
    circle(screen, (0, 0, 0), (150 + x, 330 + y), 100, 5)
    rect(screen, (255, 255, 255), (0 + x, 350 + y, 800, 300))

    lines = [
        ((50 + x, 351 + y), (248 + x, 351 + y)),
        ((50 + x, 321 + y), (248 + x, 321 + y)),
        ((55 + x, 290 + y), (243 + x, 290 + y)),
        ((75 + x, 260 + y), (223 + x, 260 + y)),
        ((75 + x, 351 + y), (75 + x, 321 + y)),
        ((150 + x, 351 + y), (150 + x, 321 + y)),
        ((225 + x, 351 + y), (225 + x, 321 + y)),
        ((105 + x, 321 + y), (105 + x, 290 + y)),
        ((180 + x, 321 + y), (180 + x, 290 + y)),
        ((95 + x, 290 + y), (95 + x, 260 + y)),
        ((160 + x, 290 + y), (160 + x, 260 + y)),
        ((210 + x, 290 + y), (210 + x, 260 + y)),
        ((105 + x, 260 + y), (105 + x, 247 + y)),
        ((180 + x, 260 + y), (180 + x, 240 + y))
    ]

    for start, end in lines:
        line(screen, (158, 158, 158), start, end, 2)

# Функция для отрисовки человека
def draw_person(x, y):
    ellipse(screen, (108, 43, 43), (530 + x, 375 + y, 120, 150))
    rect(screen, (255, 255, 255), (530 + x, 450 + y, 200, 100))

    ellipse(screen, (179, 179, 179), (550 + x, 350 + y, 80, 50))
    ellipse(screen, (108, 43, 43), (560 + x, 357 + y, 60, 37))

    circle(screen, (108, 43, 43), (565 + x, 460 + y), 15)
    circle(screen, (108, 43, 43), (615 + x, 460 + y), 15)

    ellipse(screen, (108, 43, 43), (540 + x, 465 + y, 30, 10))
    ellipse(screen, (108, 43, 43), (610 + x, 465 + y, 30, 10))

    rect(screen, (68, 25, 25), (575 + x, 400 + y, 30, 50))
    rect(screen, (68, 25, 25), (530 + x, 450 + y, 120, 10))

    ellipse(screen, (108, 43, 43), (500 + x, 400 + y, 60, 20))
    ellipse(screen, (108, 43, 43), (615 + x, 400 + y, 60, 20))

    line(screen, (0, 0, 0), (500 + x, 475 + y), (500 + x, 350 + y), 2)

    line(screen, (0, 0, 0), (580 + x, 370 + y), (575 + x, 365 + y), 2)
    line(screen, (0, 0, 0), (600 + x, 370 + y), (605 + x, 365 + y), 2)
    line(screen, (0, 0, 0), (580 + x, 380 + y), (610 + x, 380 + y), 2)

# Функция для отрисовки кошки
def draw_cat(x, y):
    ellipse(screen, (179, 179, 179), (100 + x, 450 + y, 100, 30))
    circle(screen, (179, 179, 179), (120 + x, 442 + y), 15)
    circle(screen, (255, 255, 255), (114 + x, 440 + y), 2)
    circle(screen, (255, 255, 255), (128 + x, 440 + y), 2)

    ellipse(screen, (179, 179, 179), (100 + x, 465 + y, 10, 50))
    ellipse(screen, (179, 179, 179), (115 + x, 460 + y, 10, 50))
    ellipse(screen, (179, 179, 179), (175 + x, 465 + y, 10, 50))
    ellipse(screen, (179, 179, 179), (190 + x, 460 + y, 10, 50))
    ellipse(screen, (179, 179, 179), (190 + x, 410 + y, 10, 50))

# Отрисовка нескольких юрт
draw_yurt(0, 0)  # Юрта в левом верхнем углу
draw_yurt(400, 0)  # Юрта в правом верхнем углу
draw_yurt(200, 300)  # Юрта в центре

# Отрисовка нескольких людей
draw_person(-400, -100)  # Человек в левом нижнем углу
draw_person(0, -100)  # Человек в центре внизу
draw_person(200, -100)  # Человек в правом нижнем углу

# Отрисовка нескольких кошек
draw_cat(-300, -200)  # Кошка в левом верхнем углу
draw_cat(100, -200)  # Кошка в центре вверху
draw_cat(500, -200)  # Кошка в правом верхнем углу

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
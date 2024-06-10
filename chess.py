import pygame

from parameters import (
    WHITE as W,
    HEIGHT as H,
    PLAYING_FIELD,
    colors
)
from figures import (horse_w, horse_w_d1, horse_w_d2,
                     horse, horse_d1, horse_d2)

pygame.init()

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('Chess')
pygame.display.set_icon(pygame.image.load(r'photo\\Chess_ico.png'))
sc.fill(colors['background'])


table = pygame.Surface(PLAYING_FIELD)
table.fill(colors['dark'])
num, num_x, num_y = 0, 0, 48
pygame.display.update()

for i in range(4):
    pygame.draw.rect(table, colors['white'], (num_x, 0, 47, 47))
    pygame.draw.rect(table, colors['white'], (num_y, 48, 47, 47))
    pygame.draw.rect(table, colors['white'], (num_x, 96, 47, 47))
    pygame.draw.rect(table, colors['white'], (num_y, 143, 47, 47))
    pygame.draw.rect(table, colors['white'], (num_x, 190, 47, 47))
    pygame.draw.rect(table, colors['white'], (num_y, 238, 47, 47))
    pygame.draw.rect(table, colors['white'], (num_x, 285, 47, 47))
    pygame.draw.rect(table, colors['white'], (num_y, 333, 47, 47))
    num_x += 95
    num_y += 95


def horses():
    pass


# выведение изображения
table.blit(horse_w, horse_w_d1)
table.blit(horse_w, horse_w_d2)
table.blit(horse, horse_d1)
table.blit(horse, horse_d2)

sc.blit(table, (10, 60))
pygame.display.update()

clooc = pygame.time.Clock()
fps = 30

tapmous1 = False
cord1 = cord2 = None

while True:
    for event in pygame.event.get():
        # выход из приложения
        if event.type == pygame.QUIT:
            exit()
        # Фиксирует нажатие
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            tapmous1 = True
            cord1 = event.pos
            print('down  ', cord1)
        # Фиксирует отпускание
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            cord2 = event.pos
            print('up ', cord2)

    clooc.tick(fps)

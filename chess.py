import pygame

from parameters import (
    WHITE as W,
    HEIGHT as H,
    PLAYING_FIELD,
    POS_TABLE,
    colors,
    draw_playin_field
)
from figures import draw_all_figure

pygame.init()

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('Chess')
pygame.display.set_icon(pygame.image.load(r'photo\\Chess_ico.png'))
sc.fill(colors['background'])


table = pygame.Surface(PLAYING_FIELD)
table.fill(colors['dark'])

draw_playin_field(table)


def horses():
    pass


# выведение изображения
draw_all_figure(table)

sc.blit(table, POS_TABLE)

clooc = pygame.time.Clock()
fps = 30

tapmous1 = False
cord1 = cord2 = None

while True:
    pygame.display.update()
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

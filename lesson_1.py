import pygame
from parameters import WHITE as W, HEIGHT as H, PLAYING_FIELD, colors
pygame.init()

count = 0

sc = pygame.display.set_mode((W, H))
sc.fill(colors['background'])
table = pygame.Surface(PLAYING_FIELD)
table.fill(colors['dark'])

sc.blit(table, (10, 60))

pygame.draw.rect(table, colors['white'], (10, 60, 47, 47))


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if count % 2 == 0:
                print('one', event.pos)
            else:
                print('two', event.pos)
            count += 1

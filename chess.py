# import sched
import pygame

pygame.init()

W, H = 400, 450
gray = (128, 128, 128)
white = (250, 250, 250)
dark = (10, 10, 10)
sc = pygame.display.set_mode((400, 450))
pygame.display.set_caption('Chess')
pygame.display.set_icon(pygame.image.load(r'photo\\Chess_ico.png'))
sc.fill((85, 85, 75))


horse_w = pygame.image.load(r'photo\\horse_w.png').convert_alpha()
horse_w_d = horse_w.get_rect(center=(W//2, H//2))

table = pygame.Surface((380, 380))
table.fill((0, 0, 0))
num, num_x, num_y = 0, 0, 48

# table.blit(horse_w, horse_w_d)
pygame.display.update()

for i in range(4):
    pygame.draw.rect(table, white, (num_x, 0, 47, 47), 0)
    pygame.draw.rect(table, white, (num_y, 48, 47, 47), 0)
    pygame.draw.rect(table, white, (num_x, 96, 47, 47), 0)
    pygame.draw.rect(table, white, (num_y, 143, 47, 47), 0)
    pygame.draw.rect(table, white, (num_x, 190, 47, 47), 0)
    pygame.draw.rect(table, white, (num_y, 238, 47, 47), 0)
    pygame.draw.rect(table, white, (num_x, 285, 47, 47), 0)
    pygame.draw.rect(table, white, (num_y, 333, 47, 47), 0)
    num_x += 95
    num_y += 95


def horses():
    pass


sc.blit(table, (10, 60))
pygame.display.update()

clooc = pygame.time.Clock()
fps = 30

tapmous1 = False
cord1 = cord2 = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            tapmous1 = True
            cord1 = event.pos
            print('down  ', cord1)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            cord2 = event.pos
            print('up ', cord2)

    clooc.tick(fps)

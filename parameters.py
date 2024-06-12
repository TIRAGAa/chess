from pygame import draw, Surface

WHITE = 400
HEIGHT = 450
PLAYING_FIELD = (380, 380)
POS_TABLE = (10, 60)
SIZES = (40, 40)
SIZES_P = (30, 30)

colors = {
    'gray': (128, 128, 128),
    'white': (200, 200, 200),
    'dark': (50, 50, 50),
    'background': (85, 85, 75),
    'test_red': (255, 0, 0)
}


def draw_playin_field(table: Surface):
    num_x, num_y = 0, 48
    for i in range(64):
        draw.rect(table, colors['white'], (num_x, 0, 47, 47))
        draw.rect(table, colors['white'], (num_y, 48, 47, 47))
        draw.rect(table, colors['white'], (num_x, 96, 47, 47))
        draw.rect(table, colors['white'], (num_y, 143, 47, 47))
        draw.rect(table, colors['white'], (num_x, 190, 47, 47))
        draw.rect(table, colors['white'], (num_y, 238, 47, 47))
        draw.rect(table, colors['white'], (num_x, 285, 47, 47))
        draw.rect(table, colors['white'], (num_y, 333, 47, 47))
        num_x += 95
        num_y += 95

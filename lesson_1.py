import pygame 
pygame.init()

class Window:
    def __init__(self):
        self.sc = pygame.display.set_mode((400,450))


Window()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
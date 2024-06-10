import pygame


horse_image = pygame.image.load(r'photo\\horse_w.png')
horse_w = pygame.transform.scale(horse_image, (40, 40))
horse_w_d1 = horse_w.get_rect(center=(70, 22))
horse_w_d2 = horse_w.get_rect(center=(310, 22))

horse_image = pygame.image.load(r'photo\\horse.png')
horse = pygame.transform.scale(horse_image, (40, 40))
horse_d1 = horse_w.get_rect(center=(70, 355))
horse_d2 = horse_w.get_rect(center=(310, 355))

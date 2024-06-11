import pygame

from parameters import SIZES

horse_image = pygame.image.load(r'photo\\horse_w.png')
horse_w = pygame.transform.scale(horse_image, SIZES)
horse_w_d1 = horse_w.get_rect(center=(70, 22))
horse_w_d2 = horse_w.get_rect(center=(310, 22))

horse_image = pygame.image.load(r'photo\\horse.png')
horse = pygame.transform.scale(horse_image, SIZES)
horse_d1 = horse.get_rect(center=(70, 355))
horse_d2 = horse.get_rect(center=(310, 355))

elimphant_image = pygame.image.load(r'photo\\elimphant_w.png')
elimphant_w = pygame.transform.scale(elimphant_image, SIZES)
elimphant_w_d1 = elimphant_w.get_rect(center=(120, 22))
elimphant_w_d2 = elimphant_w.get_rect(center=(260, 22))

elimphant_image = pygame.image.load(r'photo\\elimphant.png')
elimphant = pygame.transform.scale(elimphant_image, SIZES)
elimphant_d1 = elimphant_w.get_rect(center=(120, 355))
elimphant_d2 = elimphant_w.get_rect(center=(260, 355))

rook_image = pygame.image.load(r'photo\\rook_w.png')
rook_w = pygame.transform.scale(rook_image, SIZES)
rook_w_d1 = rook_w.get_rect(center=(25, 22))
rook_w_d2 = rook_w.get_rect(center=(355, 22))

rook_image = pygame.image.load(r'photo\\rook.png')
rook = pygame.transform.scale(rook_image, SIZES)
rook_d1 = rook_w.get_rect(center=(25, 355))
rook_d2 = rook_w.get_rect(center=(355, 355))

king_image = pygame.image.load(r'photo\\king_w.png')
king_w = pygame.transform.scale(king_image, SIZES)
king_w_d = king_w.get_rect(center=(215, 22))

king_image = pygame.image.load(r'photo\\king.png')
king = pygame.transform.scale(king_image, SIZES)
king_d = king_w.get_rect(center=(165, 355))

queen_image = pygame.image.load(r'photo\\queen_w.png')
queen_w = pygame.transform.scale(queen_image, SIZES)
queen_w_d = king_w.get_rect(center=(165, 22))

queen_image = pygame.image.load(r'photo\\queen.png')
queen = pygame.transform.scale(queen_image, SIZES)
queen_d = king_w.get_rect(center=(215, 355))

pawn_image = pygame.image.load(r'photo\\pawn_w.png')
pawn_w = pygame.transform.scale(pawn_image, SIZES)
pawn_w_d1 = pawn_w.get_rect(center=(25, 70))
pawn_w_d2 = pawn_w.get_rect(center=(70, 70))
pawn_w_d3 = pawn_w.get_rect(center=(120, 70))
pawn_w_d4 = pawn_w.get_rect(center=(165, 70))
pawn_w_d5 = pawn_w.get_rect(center=(215, 70))
pawn_w_d6 = pawn_w.get_rect(center=(260, 70))
pawn_w_d7 = pawn_w.get_rect(center=(310, 70))
pawn_w_d8 = pawn_w.get_rect(center=(355, 70))

pawn_image = pygame.image.load(r'photo\\pawn.png')
pawn = pygame.transform.scale(pawn_image, SIZES)
pawn_d1 = pawn.get_rect(center=(25, 307))
pawn_d2 = pawn.get_rect(center=(70, 307))
pawn_d3 = pawn.get_rect(center=(120, 307))
pawn_d4 = pawn.get_rect(center=(165, 307))
pawn_d5 = pawn.get_rect(center=(215, 307))
pawn_d6 = pawn.get_rect(center=(260, 307))
pawn_d7 = pawn.get_rect(center=(310, 307))
pawn_d8 = pawn.get_rect(center=(355, 307))

import pygame
from game import Game



g = Game()
FPS = 60
clock = pygame.time.Clock()

while g.running:
    clock.tick(FPS)
    g.curr_menu.display_menu()
    g.game_loop()
    
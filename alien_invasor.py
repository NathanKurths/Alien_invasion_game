import sys
import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800)) #cria a janela de exibição
    pygame.display.set_caption(("Alien Invasion"))
    
    bg_color=(0,0,255)
                               
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        pygame.display.flip()

run_game()
        
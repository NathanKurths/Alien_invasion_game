import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) #cria a janela de exibição
    
    pygame.display.set_caption(("Alien Invasion"))
    
    #Cria a espaçonave
    ship = Ship(ai_settings, screen)
    
    ##Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()
                                 
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
        
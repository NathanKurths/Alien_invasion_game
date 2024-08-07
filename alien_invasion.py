import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard

def run_game():
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) #cria a janela de exibição
    
    pygame.display.set_caption(("Alien Invasion"))
    
    #Cria o botão Play
    play_button = Button(ai_settings, screen, "Play")
    
    #Cria uma instância para armazenar dados estatísticos do jogo
    stats = GameStats(ai_settings)
    
    #Cria uma espaçonave, um grupo de projéteis e um grupo de alienígenas
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    #Cria uma frota de alienígenas
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #Cria instância para armazenar a pontuação
    sb = ScoreBoard(ai_settings, screen, stats)
                  
    #Inicia o laço principal do jogo               
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
        
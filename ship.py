import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    
    def __init__(self, ai_settings, screen):
        '''Inicializa a espaçonave na posição inicial'''
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Carrega a imagem da nave e obtém o seu rect
        self.image = pygame.image.load('images/ship.bmp')
        new_size = (50,50)
        self.image = pygame.transform.scale(self.image,new_size)
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Inicia cada nova nave na parte inferior da tela em sua posição atual
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        
        #Flag de movimento
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        '''Atualiza o valor do centro da espaçonave, e não o retângulo'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        
        #Atualiza o objeto rect de acordo com self.center
        self.rect.centerx = self.center
        
    def blitme(self):
        '''Desenha a nave'''
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        '''Centraliza a espaçonave na tela'''
        self.center = self.screen_rect.centerx
        
        
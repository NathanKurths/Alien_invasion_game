import pygame

class Ship():
    
    def __init__(self, screen):
        '''Inicializa a espaçonave na posição inicial'''
        self.screen = screen
        # Carrega a imagem da nave e obtém o seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Inicia cada nova nave na parte inferior da tela em sua posição atual
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        '''Desenha a nave'''
        self.screen.blit(self.image, self.rect)
        
        
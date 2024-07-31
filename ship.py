import pygame

class Ship():
    
    def __init__(self, screen):
        '''Inicializa a espaçonave na posição inicial'''
        self.screen = screen
        # Carrega a imagem da nave e obtém o seu rect
        self.image = pygame.image.load('images/ship.bmp')
        new_size = (50,50)
        self.image = pygame.transform.scale(self.image,new_size)
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Inicia cada nova nave na parte inferior da tela em sua posição atual
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #Flag de movimento
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        '''Atualiza a posição da espaçonave de acordo com a flag de movimento'''
        if self.moving_right:
            self.rect.centerx += 1
        
        if self.moving_left:
            self.rect.centerx -= 1
    def blitme(self):
        '''Desenha a nave'''
        self.screen.blit(self.image, self.rect)
        
        
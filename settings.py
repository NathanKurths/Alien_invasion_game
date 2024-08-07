class Settings():
    '''All configurations'''
    
    def __init__(self):
        # Configurações de tela
        self.screen_height = 800
        self.screen_width = 1200
        self.bg_color=(233,230,230) 
        
        # Conifugração da espaçonave
        self.ship_speed_factor = 1.5 
        self.ship_limit = 3
        
        # Configuração dos alienígenas 
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        
        # fleet_direction igual a 1 representa a direita; -1 representa a esquerda
        self.fleet_direction = 1
        
        # Configuração dos projéteis 
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
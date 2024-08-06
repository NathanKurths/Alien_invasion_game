class Settings():
    '''All configurations'''
    
    def __init__(self):
        # Configurações de tela
        self.screen_height = 800
        self.screen_width = 1200
        self.bg_color=(233,230,230) 
        self.ship_speed_factor = 1.5  
        
        #Configuração dos projéteis 
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
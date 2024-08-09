class Settings():
    '''Uma classe para armazenar todas as configurações do jogo'''
    
    def __init__(self):
        # Configurações de tela
        self.screen_height = 800
        self.screen_width = 1200
        self.bg_color=(233,230,230) 
        
        # Conifugração da espaçonave
        self.ship_limit = 3
        
        # Configuração dos alienígenas 
        self.fleet_drop_speed = 10
        
        # Configuração dos projéteis 
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        #A taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.1
        
        #A taxa com que os pontos para cada alienígena aumentam
        self.score_scale = 1.5
        
    def initialize_dynamic_settings(self):
        '''Inicializa as configurações que mudam no decorrer do jogo'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.3
        
        #fleet_direction igual a 1 representa a direita; -1 representa a esquerda
        self.fleet_direction = 1

        #Pontuação
        self.alien_points = 50
        
    def increase_speed(self):
        '''Aumenta as configurações de velocidade e os pontos para cada alienígena'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
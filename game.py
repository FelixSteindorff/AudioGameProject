import pygame

#Sets standart Parameters for all Objects in the game

class Game():
    def __init__(self):
        #init game
        pygame.init()
        #set bools for game running and playing
        self.running, self.playing = True, False
        #set bools for navigation
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        #Window Dimensions
        self.DISPLAY_W, self.DISPLAY_H = 400, 400
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        #create Window
        self.windowName = pygame.display.set_caption('Mega Game')
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        #set Font
        self.font_name = pygame.font.get_default_font()
        #Colors 
        self.BLACK, self.WHITE = (0,0,0), (255,255,255)


    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                #quit playing but keep game running
                self.playing = False
            self.display.fill(self.BLACK)
            self.draw_text('Thanks For Playing', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()


    #check key inputs
    def check_events(self):
        for event in pygame.event.get():
            #Quit
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            
            #Navigation Logic
            if event.type == pygame.KEYDOWN:
                #advance
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                #return
                if event.key == pygame.K_BACKSPACE:
                    self.START_KEY = False
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    #Reset Keypresses
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)
from numpy import False_
import pygame
from sounds import Soundloader
from menu import MainMenu,CreditsMenu,OptionsMenu, VolumeMenu,VoiceOver
import random


class Game():
    def __init__(self):
        pygame.init()
        
        #Load Menu Assets
        self.menu_image = pygame.image.load('graphics/menuAssets/MenuBackground.jpg')
        self.cursor_image = pygame.image.load('graphics/menuAssets/cursor1.png')
        self.cursor_image_resized = pygame.transform.scale(self.cursor_image, (50,80))
        self.cursor_image_resized.set_colorkey(None)
        
        #Load Game Assets
        self.scissor_player = pygame.image.load('graphics/gameAssets/Scissors_Player.png')
        self.scissor_com = pygame.image.load('graphics/gameAssets/Scissors_Cp.png')

        self.clock = pygame.time.Clock()
        
        #variables to track if playing or running 
        self.running, self.playing = True, False
        
        #bools for Key Pressed
        self.R_KEY, self.S_KEY, self.P_KEY, self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False , False,False,False, False, False, False, False
        
        #surface size varibles 
        self.DISPLAY_W, self.DISPLAY_H = 800, 600
        
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        
        #init Menus on start
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.volume = VolumeMenu(self)
        self.curr_menu = self.main_menu
        self.RockPaperScissors = RockPaperScissors(self)

        
    
    
    
    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= False
            self.RockPaperScissors.display_game()
            #self.draw_text('Thanks for Playing', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0,0))
            self.reset_keys()

    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
                if event.key == pygame.K_r:
                    self.R_KEY = True
                if event.key == pygame.K_s:
                    self.S_KEY = True
                if event.key == pygame.K_p:
                    self.P_KEY = True
                

    def reset_keys(self):
        self.R_KEY, self.S_KEY, self.P_KEY, self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False , False,False,False, False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)
        pygame.display.flip()

class RockPaperScissors():
    from sounds import Soundloader

    def __init__(self, game):
        self.game = game
        self.score = 0
        self.score_sounds = Soundloader()
        self.game_running = True
        #player side of screen
        self.player_side_w, self.mid_h = self.game.DISPLAY_W / 2.5, self.game.DISPLAY_H / 2
        self.player_side_symbol_x,self.player_side_symbol_y =  self.player_side_w -100, self.mid_h
        self.score_x, self.score_y = self.player_side_w-250, self.mid_h-280
        self.choices = {"Rock","Scissors", "Paper"}
        self.computer_choice = self.getComputerChoice()
        self.player_choice = self.getPlayerChoice
        self.curr_player_Symbol= 0


    #function to render the display and reset key inputs
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

    
    def display_game(self):
        while self.game.playing == True:
            self.game.check_events()
            self.render_Shit()
            self.game.draw_text(f'Score: {str(self.score)}', 30, self.score_x, self.score_y)
            self.gameLogic()
            self.blit_screen()
            pygame.display.flip()


    def check_input(self):
        if self.game.R_KEY:
            self.curr_player_Symbol = 1
            return "Rock"
        elif self.game.S_KEY:
            self.curr_player_Symbol = 2
            return "Scissors"
        elif self.game.P_KEY:
            self.curr_player_Symbol = 3
            return "Paper"

    #under construction lol
    def render_Shit(self):
        if self.curr_player_Symbol == 2:
            self.game.display.blit(self.game.scissor_player, (self.player_side_symbol_x,self.player_side_symbol_y))    
        else:
            self.game.display.fill((220,220,220))
        
    def getPlayerChoice(self):
        return self.check_input()
    

    def getComputerChoice(self):
        self.computer_choice = random.choice(list(self.choices))
        return self.computer_choice
    
    #params computer_choice and playerchoice are compared and result is returned 
    def gameRules(self, computer_choice, player_choice):
        result = ''
        if player_choice != None:
            if computer_choice == player_choice:
                result = 'tie'
                print(f'tie  Computer:{computer_choice} : You {player_choice}')
            elif computer_choice == 'Scissors' and player_choice == 'Rock':
                result = 'win'
                print(f'ROCK crushes SCISSORS! You win!Computer:{computer_choice} : You {player_choice}')
            elif computer_choice == 'Paper' and player_choice == 'Scissors': 
                result = 'win'
                print(f'SCISSORS cut PAPER! You win!Computer:{computer_choice} : You {player_choice}')
            elif computer_choice == 'Rock' and player_choice == 'Paper': 
                result = 'win'
                print(f'PAPER covers Rock! You win! Computer:{computer_choice} : You {player_choice}')  
            else: 
                result = 'lose'
                print(f'You lose! Computer:{computer_choice} : You {player_choice}')
            self.game_running = False
            
        return result

    #gets result of gameRules and increases/decreases score depending on result
    def gameLogic(self):
        self.computer_choice = self.getComputerChoice() 
        self.player_choice = self.getPlayerChoice()
        
        result = self.gameRules(self.computer_choice, self.player_choice)

        if self.player_choice:
            if  result == 'win':
                self.score +=1
                self.score_sounds.scoreUpSound()
            elif result == 'lose':
                self.score -=1
                self.score_sounds.scoreDownSound()
            elif result == 'tie':
                self.score = self.score






   


    

    

 


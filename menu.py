import pygame
import accessible_output2.outputs.auto


class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        #varible to keep display running
        self.run_display = True
        self.curor_rect = pygame.Rect(0, 0, 20,20)
        #offset curor to the left
        self.offset = -100


    def draw_cursor(self):
        self.game.draw_text('*', 15, self.curor_rect.x , self.curor_rect.y)

    def blit_scree(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        #set Start as default position on startup
        self.state = "Start"
        #Positions for Buttons
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.quitx, self.quity = self.mid_w, self.mid_h + 50
        self.curor_rect.midtop = (self.startx, self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.game.display.fill(self.game.BLACK)
            self.draw_text('Heftiges Spiel', 20, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 -20)
            self.draw_text('Start Game', 20, self.startx, self.starty)
            self.draw_text('Quit', 20, self.quitx, self.quity)
            self.draw_cursor()

    def move_cursor(self):
        o = accessible_output2.outputs.auto.Auto()
        
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.curor_rect.midtop = (self.quitx + self.offset, self.quity)
        
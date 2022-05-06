
import pygame
import accessible_output2.outputs.auto
from sounds import Soundloader
from pygame import mixer 
 
class VoiceOver():
    def __init__(self):
        self.VoiceEnabled = True
        self.voice = accessible_output2.outputs.auto.Auto()

    
    def read(self, text):
        if self.VoiceEnabled == True:
            self.voice.speak(text, interrupt= True)
            self.voice.braille(text)
        
class Menu():
    def __init__(self, game):
        self.game = game
        self.soundloader = Soundloader()
        self.VoiceOver = VoiceOver()
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100
        
       

    def draw_cursor(self):
        self.game.draw_text('*', 25, self.cursor_rect.x, self.cursor_rect.y)
        pygame.display.flip()

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 90
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 120
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 200
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Main Menu', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start Game", 30, self.startx, self.starty)
            self.game.draw_text("Options", 30, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 30, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()
            pygame.display.flip()
            


    def move_cursor(self):
        
        if self.game.DOWN_KEY:
            
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            self.VoiceOver.read(self.state)
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            self.VoiceOver.read(self.state)
        pygame.display.flip()
        

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.soundloader.forwardSound()
                self.game.playing = True
            elif self.state == 'Options':
                self.soundloader.forwardSound()
                self.game.curr_menu = self.game.options
                if self.state == 'Volume':
                    self.game.curr_menu = self.game.volume
            elif self.state == 'Credits':
                self.soundloader.forwardSound()
                self.game.curr_menu = self.game.credits
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 60
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def draw_test(self):
        self.game.draw_text('*', 25, self.cursor_rect.x, self.cursor_rect.y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Volume", 30, self.volx, self.voly)
            self.game.draw_text("Controls", 30, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()
            

    def check_input(self):
        if self.game.START_KEY:
            self.soundloader.forwardSound()
        if self.game.BACK_KEY:
            self.soundloader.backwardSound()
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
                self.VoiceOver.read(self.state)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
                self.VoiceOver.read(self.state)
        elif self.game.START_KEY:
            if self.state == 'Volume':
                self.game.curr_menu = self.game.volume
            self.run_display = False
                


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.soundloader.forwardSound()
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made by Felix Steindorf and Bastian Brück', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()

class VolumeMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Game Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        self.soundloader = Soundloader()
        self.slidx, self.slidy= self.mid_w, self.mid_h + 20
        self.slider = 1*100
        self.VolSlide = pygame.Rect(self.slidx - 50, self.slidy, self.slider, 15)

    def check_input(self):
        self.move_cursor()
        if self.game.BACK_KEY:
            self.soundloader.backwardSound()
            self.game.curr_menu = self.game.options
            self.run_display = False
        elif self.game.START_KEY:
            self.soundloader.forwardSound()
                    #num = float(input("Get Vol"))
                    #self.soundloader.forward.set_volume(num)
                    #self.soundloader.backward.set_volume(num)
            self.run_display = False

    def move_cursor(self):
        if self.game.START_KEY:
            self.state == 'VolumeSlider'
            self.cursor_rect.midtop = (self.slidx + self.offset, self.slidy)
            self.VoiceOver.read("Menu Sound")
        if self.game.LEFT_KEY:
            if(self.slider > 0):
                self.state = 'Minus'
                self.slider -= 10
                for sounds in self.soundloader.menuSounds:
                    sounds.set_volume(self.slider/100)
                self.VolSlide = pygame.Rect(self.slidx - 50, self.slidy, self.slider, 15)
                self.VoiceOver.read(str(self.slider))
            else:
                self.slider = 0
            print(self.soundloader.forward.get_volume())
        if self.game.RIGHT_KEY:
            if(self.slider < 100):
                self.state = 'Plus'
                self.slider += 10
                #self.soundloader.forward.set_volume(self.slider/100)
                for sounds in self.soundloader.menuSounds:
                    sounds.set_volume(self.slider/100)
                self.VolSlide = pygame.Rect(self.slidx - 50, self.slidy, self.slider, 15)
                self.VoiceOver.read(str(self.slider))
                print(self.soundloader.forward.get_volume())
            else:
                self.slider = 100  
       

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Volume Settings', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            pygame.draw.rect(self.game.display, (255,255,255), self.VolSlide)
            self.draw_cursor()
            self.blit_screen()

    
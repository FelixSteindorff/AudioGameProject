
import pygame
import accessible_output2.outputs.auto
from sounds import Soundloader
from pygame import mixer


#var for Voice Over (must be restructured later...)
global VoiceEnabled 
VoiceEnabled = True

class VoiceOver():
    def __init__(self):
        
        self.voice = accessible_output2.outputs.auto.Auto()

    
    def read(self, text):
        if VoiceEnabled == True:
            self.voice.speak(text, interrupt= True)
            self.voice.braille(text)
        else:
            pass
        
class Menu():
    def __init__(self, game):
        self.game = game
        self.soundloader = Soundloader()
        self.VoiceOver = VoiceOver()
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100
       
    #draws the cursor to the screen   
    def draw_cursor(self):
        self.game.display.blit(self.game.cursor_image_resized, (self.cursor_rect.x-30,self.cursor_rect.y-45))
        #self.game.draw_text('*', 25, self.cursor_rect.x, self.cursor_rect.y)
        pygame.display.flip()

    #function to render the display and reset key inputs
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        #Variable to track the current Position in Menu
        self.state = "Start"
        
        #Positions of the Menu Items
        self.startx, self.starty = self.mid_w, self.mid_h + 90
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 120
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 200
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        
    #show MainMenu
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.blit(self.game.menu_image, (0,0))
            self.game.draw_text('Main Menu', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start Game", 30, self.startx, self.starty)
            self.game.draw_text("Options", 30, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 30, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()
            pygame.display.flip()
            

    #function to move cursor
    def move_cursor(self):
        
        if self.game.DOWN_KEY:
            #get current state and update it on self.game.<KEY_PRESSED>
            if self.state == 'Start':
                #draw cursor to current selected Item
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                #draw cursor to current selected Item
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                #draw cursor to current selected Item
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            #obj VoiceOver to read
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

#OptionsMenu extends Menu
class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 60
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)


    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.blit(self.game.menu_image, (0,0))
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
            self.game.display.blit(self.game.menu_image, (0,0))
            self.game.draw_text('Credits', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made by Felix Steindorf and Bastian Brück', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()

class VolumeMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Menu Sound'
        #Position of Voice enable/disable Item
        self.disableVoicex,self.disableVoicey = self.mid_w, self.mid_h + 70
        #obj to import Sound Assets 
        self.soundloader = Soundloader()
        #slider position
        self.slidx, self.slidy= self.mid_w, self.mid_h + 20
        self.cursor_rect.midtop = (self.slidx + self.offset, self.slidy)
        #Variable to show current slider value *100 bec sound is measured from 0 - 1...
        self.slider = 1*100
        #Slider Object (draws rectange) 
        self.VolSlide = pygame.Rect(self.slidx - 50, self.slidy, self.slider, 15)

    def check_input(self):
        #checks if VoiceOver is enabled
        global VoiceEnabled 
        self.move_cursor()
        if self.game.BACK_KEY:
            self.soundloader.backwardSound()
            self.game.curr_menu = self.game.options
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Menu Sound':
                self.state = 'Disable Voice'
                self.cursor_rect.midtop = (self.disableVoicex-50 + self.offset, self.disableVoicey)
                self.VoiceOver.read(self.state)
            elif self.state == 'Disable Voice':
                self.state = 'Menu Sound'
                self.cursor_rect.midtop = (self.slidx + self.offset, self.slidy)
                self.VoiceOver.read(self.state)
            self.soundloader.forwardSound()
        elif self.state == 'Disable Voice' and self.game.START_KEY :
            #Statement to enable and disable Voice Over
            if VoiceEnabled == True:
                self.VoiceOver.read('VoiceOver disabled')
                VoiceEnabled = False
            elif VoiceEnabled == False:
                VoiceEnabled = True
                self.VoiceOver.read('VoiceOver enabled')
        
        self.run_display = False

    def move_cursor(self):
        if self.game.LEFT_KEY:
            #Statement to decrease menuSounds volume and Slider var(to visualize current volume)
            if(self.slider > 0):
                self.slider -= 10
                for sounds in self.soundloader.menuSounds:
                    sounds.set_volume(self.slider/100)
                self.VolSlide = pygame.Rect(self.slidx - 50, self.slidy, self.slider, 15)
                self.VoiceOver.read(str(self.slider))
            else:
                self.slider = 0
            print(self.soundloader.forward.get_volume())
        if self.game.RIGHT_KEY:
            #Statement to increase menuSounds volume and Slider var(to visualize current volume)
            if(self.slider < 100):
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
            self.game.display.blit(self.game.menu_image, (0,0))
            self.game.draw_text('Volume Settings', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            #draw Volume Slider
            pygame.draw.rect(self.game.display, (255,255,255), self.VolSlide)
            self.game.draw_text("Disable Voice", 30, self.disableVoicex, self.disableVoicey)
            self.draw_cursor()
            self.blit_screen()

    

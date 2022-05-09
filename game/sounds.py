from turtle import back
import pygame
from pygame.locals import *



class Soundloader():  
    pygame.mixer.init()
    pygame.init()
   
    
    forward = pygame.mixer.Sound("sounds/click.wav")
    backward = pygame.mixer.Sound("sounds/click_rev.wav")
    menuSounds = [forward, backward]

    #play forward sound to advance in Menu
    def forwardSound(self):
        forwardCh = self.forward.play()
        return forwardCh

    #play backward sound to go to previous menu
    def backwardSound(self):
        backwardCh = self.backward.play()
        return backwardCh

   
   
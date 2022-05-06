from turtle import back
import pygame
from pygame.locals import *



class Soundloader():  
    pygame.mixer.init()
    pygame.init()
   
    
    forward = pygame.mixer.Sound("sounds/click.wav")
    backward = pygame.mixer.Sound("sounds/click_rev.wav")
    menuSounds = [forward, backward]

    def forwardSound(self):
        forwardCh = self.forward.play()
        return forwardCh

    def backwardSound(self):
        backwardCh = self.backward.play()
        return backwardCh

   
   
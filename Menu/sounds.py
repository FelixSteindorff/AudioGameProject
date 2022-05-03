import pygame
from pygame.locals import *



class Soundloader():  
    pygame.mixer.init()
    forward = pygame.mixer.Sound("Sounds/click.wav")
    backward = pygame.mixer.Sound("Sounds/click_rev.wav")


    def forwardSound(self):
        forwardCh = self.forward.play()
        return forwardCh

    def backwardSound(self):
        backwardCh = self.backward.play()
        return backwardCh

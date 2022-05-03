import pygame
from pygame.locals import *



class Soundloader():  
    pygame.mixer.init()
    forward = pygame.mixer.Sound("sounds/click.wav")
    backward = pygame.mixer.Sound("sounds/click_rev.wav")


    def forwardSound(self):
        forwardCh = self.forward.play()
        return forwardCh

    def backwardSound(self):
        backwardCh = self.backward.play()
        return backwardCh

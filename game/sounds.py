import pygame
from pygame.locals import *



class Soundloader():  
    pygame.mixer.init()
    pygame.init()
   
    
    forward = pygame.mixer.Sound("sounds/click.wav")
    backward = pygame.mixer.Sound("sounds/click_rev.wav")
    
    score_Up = pygame.mixer.Sound("sounds/ScoreUP.wav")
    score_Down = pygame.mixer.Sound("sounds/ScoreDown.wav")
    score_Up.set_volume(0.3)

    menuSounds = [forward, backward]

    #play ScoreDown
    def scoreDownSound(self):
        score_Down_Ch = self.score_Down.play()
        return score_Down_Ch 

    #play ScoreUp
    def scoreUpSound(self):
        score_Up_Ch = self.score_Up.play()
        return score_Up_Ch, 


    #play forward sound to advance in Menu
    def forwardSound(self):
        forwardCh = self.forward.play()
        return forwardCh

    #play backward sound to go to previous menu
    def backwardSound(self):
        backwardCh = self.backward.play()
        return backwardCh

   
   
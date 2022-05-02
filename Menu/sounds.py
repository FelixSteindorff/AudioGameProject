from pygame import mixer as m

class Soundloader():  

    def loadSound(self,file):
        m.music.load(file)
        m.music.play()
    
    
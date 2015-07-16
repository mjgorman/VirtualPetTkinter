#!/usr/bin/python
from random import randint
from time import sleep

class digimon(object):
    def __init__(self, name):
        self.name = "digi-egg"
        self.str = 1
        self.spd = 1 
        self.int = 1
        self.level = 0
        self.__birth(name)

    def __prompt(self, output):
        print "<<", self.name, ">>", output
    def __pause(self, min=1, max=3):
        sleep(randint(min, max))
    def __chance(self):
        if randint(1, 3) == 3:
            return True
        return False
    def stats(self):
        levels = ['In-Training', 'Rookie', 'Champion', 'Ultimate','Mega' ]
        print "<<Digivice>> BEEP BEEP BEPP"
        print " ___________"
        print " {}".format(levels[self.level]) 
        print " ___________"
        print "| str: {:3d}  |".format(self.str)
        print "| spd: {:3d}  |".format(self.spd)
        print "| int: {:3d}  |".format(self.int)
        print "|___________|"

    def __birth(self, name):
        self.__prompt('An egg sits before you. Moving ever so slightly back and forth')
        self.__pause()
        count = 0 
        while count <= 5:
            if self.__chance():
               self.__prompt('The Egg bounces, whatever is inside seems to be getting stronger')
               self.str += 1
               self.__pause()
            else:
               self.__prompt('The Egg rocks back and forth faster and faster')
               self.spd += 1
               self.__pause()
            count += 1
        self.__prompt('The Egg stopped all the sudden')
        self.__hatch(name)
        
    def __hatch(self, name):
        self.__prompt('*Crack*')
        self.__pause()
        self.__prompt('*Crack, Crack*')
        self.__pause()
        self.__prompt('A strange creature emerges from the egg')
        self.__pause()
        self.name = name
        self.__prompt('"Hi! I\'m ' + self.name + '"')
        
if __name__ == '__main__':
    koromon = digimon("koromon")
    koromon.stats()

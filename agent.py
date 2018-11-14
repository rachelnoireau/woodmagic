from enum import Enum

class Action(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4
    USE_CRISTAL = 5
    TAKE_CRISTAL = 6
    TAKE_PORTAL = 7



class Agent:

    def __init__(self):
        self.posX = 0
        self.posY = 0
        self.nbr_dead = 0
        self.nbr_cristal = 0
        self.action = Action


    def is_dead(self):
        self.nbr_dead += 1

    def get_pos(self):
        return (self.posX , self.posY)


    def go_right(self): #juste pour tester
        self.posY += 1


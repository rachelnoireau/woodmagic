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

    def __init__(self, inference_engine):
        self.posX = 0
        self.posY = 0
        self.nbr_dead = 0
        self.nbr_cristal = 0

        self.__inference_engine = inference_engine
        self.next_area_to_visit = None
        self.next_action = None
        self.visited_areas = []
        self.frontier = []
        self.unknown_cells = []

        self.knowledge_base = []

        self.level = 0    #the size 3*3 ici level 0
        self.action = Action

    def execute_action(self):
        self.next_action.execute()

    def plan_next_action(self):
        # self.next_area_to_visit = self.__inference_engine.plan(self.visited_areas, self.frontier, self.unknown_cells)
        return None
        # Deduce next action

    def next_level(self):
        self.level += 1

    def set_pos(self, x, y):
        self.posX = x
        self.posY = y

    def is_dead(self):
        self.nbr_dead += 1

    def get_pos(self):
        return (self.posX , self.posY)

    def take_cristal(self):
        self.nbr_cristal += 1


    def go_right(self): #juste pour tester
        self.posY += 1


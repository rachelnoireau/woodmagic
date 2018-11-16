from enum import Enum
from area import Area
import math


class Action(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4
    USE_CRISTAL = 5
    TAKE_CRISTAL = 6
    TAKE_PORTAL = 7


class Agent:

    def __init__(self, inference_engine, wood):
        self.posX = 0
        self.posY = 0
        self.nbr_dead = 0
        self.wood = wood

        self.inference_engine = inference_engine
        self.next_area_to_visit = None
        self.next_action = None
        self.visited_areas = []

        # Frontier is split between safe areas, one array for potential monster, one for potential holes
        self.frontier = [[], [], []]
        self.current_area = self.wood.get_area_at_position(self.posX, self.posY)
        self.target_area = None

        self.level = 0    #the size 3*3 ici level 0
        self.action = Action

    def execute_action(self):
        # self.action_queue.put(self.next_action)
        if self.next_action == Action.UP:
            self.move_to(self.current_area.up_neighbour)
        elif self.next_action == Action.DOWN:
            self.move_to(self.current_area.down_neighbour)
        elif self.next_action == Action.RIGHT:
            self.move_to(self.current_area.right_neighbour)
        elif self.next_action == Action.LEFT:
            self.move_to(self.current_area.left_neighbour)
        elif self.next_action == Action.USE_CRISTAL:
            self.next_area_to_visit.received_cristal()
        elif self.next_action == Action.TAKE_PORTAL:
            self.take_portal()

        action_performed = self.next_action
        self.next_action = None
        self.performance = self.update_performance()
        return action_performed

    def move_to(self, area):
        if not area:
            print("Error, tried to move where there is no area")
            return
        self.visited_areas.append(self.current_area)
        self.current_area = area
        self.posX = area.posX
        self.posY = area.posY
        self.remove_from_frontier(self.current_area)
        # TODO: Remove this area from frontier if it's in

    def remove_from_frontier(self, area):
        for arealist in self.frontier:
            if area in arealist:
                arealist.remove(area)

    def take_portal(self):
        if self.current_area.is_cristal:
            self.level += 1

    def update_performance(self):
        return None

    def plan_next_action(self):
        self.inference_engine.run(self.current_area, self.frontier)
        self.next_area_to_visit = self.first_area_in_frontier()
        self.next_action = self.get_action_to_target()

    def first_area_in_frontier(self):
        if len(self.frontier[0]) > 0:  # Safe rooms
            return self.frontier[0][0]
        if len(self.frontier[1]) > 0:  # Rooms with danger of monster
            return self.frontier[1][0]
        if len(self.frontier[2]) > 0:  # Rooms with danger of hole
            return self.frontier[2][0]
        return None

    def get_action_to_target(self):
        if self.current_area == self.next_area_to_visit:
            # We don't want to move -> we are on the portal
            print("take the portal")
            return Action.TAKE_PORTAL
        print(self.current_area.neighbors)
        print(self.next_area_to_visit.posX)
        print(self.next_area_to_visit.posY)
        if self.next_area_to_visit in self.current_area.neighbors:
            # Direct neighbor
            print("ici")

            if self.next_area_to_visit.is_risky_of_monster():
                return Action.USE_CRISTAL
            if self.next_area_to_visit.posX > self.current_area.posX:
                return Action.RIGHT
            if self.next_area_to_visit.posX < self.current_area.posX:
                return Action.LEFT
            if self.next_area_to_visit.posY < self.current_area.posY:
                return Action.UP
            else:
                return Action.DOWN
        # Target is further
        return self.get_next_move_toward_target()

    def get_next_move_toward_target(self):
        ok_right = self.ok_for_itinerary(self.current_area.right_neighbour)
        ok_left = self.ok_for_itinerary(self.current_area.left_neighbour)
        ok_up = self.ok_for_itinerary(self.current_area.up_neighbour)
        ok_down = self.ok_for_itinerary(self.current_area.down_neighbour)

        if self.next_area_to_visit.posX > self.current_area.posX:
            if ok_right:
                return Action.RIGHT
        if self.next_area_to_visit.posX < self.current_area.posX:
            if ok_left:
                return Action.LEFT
        if self.next_area_to_visit.posY < self.current_area.posY:
            if ok_up:
                return Action.UP
        else:
            if ok_down:
                return Action.DOWN

    def ok_for_itinerary(self, area):
        return area is not None and area in self.visited_areas and area.is_safe()

    def next_level(self):
        self.level += 1

    def set_pos(self, x, y):
        self.posX = x
        self.posY = y

    def is_dead(self):
        self.nbr_dead += 1

    def get_pos(self):
        return (self.posX , self.posY)

    #Pour aller de position a next_visited_area
    def short_way(self):
        nbcase = 0
        case = self.current_area
        visited_node = []
        distance = []
        for node in self.visited_areas :
            distance.add(math.inf)
        go_up = False
        go_left = False
        if self.current_area.posX - self.next_area_to_visit.posX > 0 :
            go_left = True
        if self.current_area.posY - self.next_area_to_visit.posY > 0:
            go_up = True
        while case != self.next_area_to_visit :
            while case.posX != self.next_area_to_visit.posX :
                if go_left :
                    for node in self.visited_areas :
                        if node.posX == case.posX+1 & node.posY == case.posY :
                            case = node
                else :
                    for node in self.visited_areas:
                        if node.posX == case.posX -1 & node.posY == case.posY:
                            case = node
                nbcase+1
                while case.posY != self.next_area_to_visit.posY:
                    if go_up:
                        for node in self.visited_areas:
                            if node.posX == case.posX  & node.posY == case.posY +1:
                                case = node
                    else:
                        for node in self.visited_areas:
                            if node.posX == case.posX  & node.posY == case.posY -1:
                                case = node
                    nbcase + 1

               # visited_node.add(case)

        return nbcase

from wood import Wood
from display import Display
from agent import Agent

class Simulation:
    def __init__(self):
        self.agent = Agent()
        self.size = self.agent.level +3
        self.wood = Wood(self.size)
        #while(True):
        #self.agent.set_pos(0,0)
        #while not(self.wood.grid[self.agent.get_pos()[0]][self.agent.get_pos()[1]].get_portal()):
        #self.display = Display(self.size, self.agent.get_pos(),self.agent)


        #self.display.add_grid(self.wood.get_grid())
        #self.display.create_button(self.agent)
        #print(self.agent.get_pos())
        #self.display.start_loop()

        #self.agent.next_level()

        self.display = Display(self.agent, self.wood)



if __name__ == '__main__':
    Simulation()

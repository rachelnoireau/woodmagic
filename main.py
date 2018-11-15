from wood import Wood
from display import Display
from agent import Agent
from inference_engine import InferenceEngine
from inference import Inference


class Simulation:
    def __init__(self):

        # normal_case = Inference([InferenceEngine.is_normal], [InferenceEngine.go_ahead])
        # monster_case = Inference([InferenceEngine.is_monster_on_area], [InferenceEngine.agent_death])
        # hole_case = Inference([InferenceEngine.is_hole_on_area], [InferenceEngine.agent_death])
        # wind_case1 = Inference([InferenceEngine.is_windy, InferenceEngine.first_visit], [InferenceEngine.go_back])
        # wind_case2 = Inference([InferenceEngine.is_windy, InferenceEngine.not_first_visit], [InferenceEngine.go_ahead])
        # poop_case1 = Inference([InferenceEngine.is_pooped, InferenceEngine.first_visit], [InferenceEngine.go_back])
        # poop_case2 = Inference([InferenceEngine.is_pooped, InferenceEngine.not_first_visit],
        #                      [InferenceEngine.throw_stone, InferenceEngine.go_back])
        # gate_case = Inference([InferenceEngine.is_portal], [InferenceEngine.take_portal])
        # rule_set = [normal_case, monster_case, hole_case, wind_case1, wind_case2, poop_case1, poop_case2, gate_case]

        # When inferences only return new knowledge on the world
        wind_case = Inference([InferenceEngine.neighbors_arent_risky], [])
        rule_set = [wind_case]

        inference_engine = InferenceEngine(rule_set)
        self.agent = Agent(inference_engine)
        self.size = self.agent.level + 3

        self.size = 3
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

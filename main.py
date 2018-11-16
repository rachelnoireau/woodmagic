from wood import Wood
from display import Display
from agent import Agent
from inference_engine import InferenceEngine
from inference import Inference


class Simulation:
    def __init__(self):

        # When inferences only return new knowledge on the world
        normal_case = Inference([InferenceEngine.has_safe_unexplored_neighbour], [InferenceEngine.explore_safe_neighbors])
        fell_case = Inference([InferenceEngine.is_windy, InferenceEngine.agent_fell_in_neighbor],
                              [InferenceEngine.agent_knows_hole_neighbor])
        wind_case = Inference([InferenceEngine.is_windy], [InferenceEngine.mark_neighbors_risky_of_hole])
        poop_case = Inference([InferenceEngine.is_pooped], [InferenceEngine.mark_neighbors_risky_of_monster])
        area_cleaned = Inference([InferenceEngine.is_pooped, InferenceEngine.threw_stone_on_neighbor],
                                 [InferenceEngine.mark_neighbor_safe_of_monster])
        # gate_case = Inference([InferenceEngine.has_portal], [InferenceEngine.take_portal])

        rule_set = [normal_case, fell_case, poop_case, wind_case, area_cleaned]
        inference_engine = InferenceEngine(rule_set)

        self.size = 3

        self.wood = Wood(self.size)
        self.agent = Agent(inference_engine, self.wood)
        self.display = Display(self.agent, self.wood)


if __name__ == '__main__':
    Simulation()

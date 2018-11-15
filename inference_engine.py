

class InferenceEngine:
    def __init__(self, inferences):
        self.__inferences = inferences

    def plan(self):
        for inference in self.__inferences:
            if inference.can_execute():
                inference.execute()

    @staticmethod
    def neighbors_arent_risky(area, explored, frontier):
        for neighbor in area.neighbors:
            if not neighbor.was_visited and not neighbor.is_risky_of_monster and not neighbor.is_risky_of_hole:
                frontier.insert(0, neighbor)  # Add this area at the beginning of the frontier as it is closer and safe

    # @staticmethod
    # def

    # Actions
    @staticmethod
    def go_ahead():
        return None

    @staticmethod
    def go_back():
        return None

    @staticmethod
    def agent_death():
        return None

    @staticmethod
    def take_portal():
        return None

    @staticmethod
    def throw_stone():
        return None

    # Premises
    @staticmethod
    def first_visit(area):
        return not area.was_visited

    @staticmethod
    def not_first_visit(area):
        return area.was_visited

    @staticmethod
    def is_monster_on_area(area):
        return area.is_monster

    @staticmethod
    def is_hole_on_area(area):
        return area.is_hole

    @staticmethod
    def is_visited(area):
        return area.is_windy

    @staticmethod
    def is_windy(area):
        return area.is_next_to_hole

    @staticmethod
    def is_pooped(area):
        return area.is_next_to_monster

    @staticmethod
    def is_portal(area):
        return area.is_portal

    @staticmethod
    def is_normal(area):
        return not (area.is_monster or area.is_hole or area.is_next_to_monster or area.is_next_to_hole or
                    area.is_portal or area.is_cristal)

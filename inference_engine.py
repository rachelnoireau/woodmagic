

class InferenceEngine:
    def __init__(self, inferences):
        self.__inferences = inferences

    def run(self, current_context, params):
        new_fact_discovered = True
        while new_fact_discovered:
            new_fact_discovered = False
            for rule in self.__inferences:
                if rule.can_apply(current_context, params):
                    rule.apply(current_context, params)
                    new_fact_discovered = True

    @staticmethod
    def has_portal(area, frontier):
        return area.is_portal

    @staticmethod
    def has_safe_unexplored_neighbour(area, frontier):
        for neighbor in area.neighbors:
            print((not neighbor.was_visited), (not neighbor.is_risky_of_monster()), (not neighbor.is_risky_of_hole()))
            if (not neighbor.was_visited) and (not neighbor.is_risky_of_monster()) and (not neighbor.is_risky_of_hole()):
                return True
        return False

    @staticmethod
    def explore_safe_neighbors(area, frontier):
        for neighbor in area.neighbors:
            if (not neighbor.was_visited) and (not neighbor.is_risky_of_monster()) and (not neighbor.is_risky_of_hole()):
                # Add this area at the beginning of the frontier as it is closer and safe
                (frontier[0]).insert(0, neighbor)

    @staticmethod
    def mark_neighbors_risky_of_hole(area, frontier):
        for neighbor in area.neighbors:
            if not neighbor.was_visited:
                neighbor.mark_risky_of_hole()
                frontier[2].insert(0, neighbor)

    @staticmethod
    def mark_neighbors_risky_of_monster(area, frontier):
        for neighbor in area.neighbors:
            if not neighbor.was_visited:
                neighbor.mark_risky_of_monster()
                frontier[1].insert(0, neighbor)

    @staticmethod
    def mark_safe(area, frontier):
        area.mark_safe()



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
    def take_portal(area, frontier):
        return None

    @staticmethod
    def throw_stone():
        return None

    # Premises
    @staticmethod
    def first_visit(area, frontier):
        return not area.was_visited

    @staticmethod
    def not_first_visit(area, frontier):
        return area.was_visited

    @staticmethod
    def is_monster_on_area(area, frontier):
        return area.is_monster

    @staticmethod
    def is_hole_on_area(area, frontier):
        return area.is_hole

    @staticmethod
    def is_visited(area, frontier):
        return area.is_windy

    @staticmethod
    def is_windy(area, frontier):
        return area.is_next_to_hole

    @staticmethod
    def is_pooped(area, frontier):
        return area.is_next_to_monster

    @staticmethod
    def is_portal(area, frontier):
        return area.is_portal

    @staticmethod
    def is_normal(area, frontier):
        return not (area.is_monster or area.is_hole or area.is_next_to_monster or area.is_next_to_hole or
                    area.is_portal or area.is_cristal)

    @staticmethod
    def is_risky_of_monster(area, frontier):
        return area.is_risky_of_monster()

    @staticmethod
    def threw_stone(area, frontier):
        return area.received_stone()

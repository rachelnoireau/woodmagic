

class InferenceEngine:
    def __init__(self, inferences):
        self.__inferences = inferences

    def run(self, current_context, params):
        for rule in self.__inferences:
            rule.reset()

        new_fact_discovered = True
        while new_fact_discovered:
            new_fact_discovered = False
            for rule in self.__inferences:
                if rule.can_apply(current_context, params):
                    print("Area ", current_context.posX, current_context.posY)
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
        print("Explore safe neighbors")
        for neighbor in area.neighbors:
            if (not neighbor.was_visited) and (not neighbor.is_risky_of_monster()) and (not neighbor.is_risky_of_hole()):
                # Add this area at the beginning of the frontier as it is closer and safe
                print("I have safe neighbor", neighbor.posX, neighbor.posY)
                InferenceEngine.add_to_frontier(neighbor, 0, frontier)

    @staticmethod
    def mark_neighbors_risky_of_hole(area, frontier):
        print("Mark neighbors risk hole")
        for neighbor in area.neighbors:
            if not neighbor.was_visited and not neighbor.user_fell_in:
                neighbor.mark_risky_of_hole()
                InferenceEngine.add_to_frontier(neighbor, 2, frontier)

    @staticmethod
    def mark_neighbors_risky_of_monster(area, frontier):
        print("Mark neighbors risk monster")
        for neighbor in area.neighbors:
            print(neighbor.posX, neighbor.posY, "Was visited ? ", neighbor.was_visited, " cristal ?", neighbor.received_cristal())
            if (not neighbor.was_visited) and (not neighbor.received_cristal()):
                print("Marking ", neighbor.posX, neighbor.posY, " as risky for monster")
                neighbor.mark_risky_of_monster()
                InferenceEngine.add_to_frontier(neighbor, 1, frontier)

    @staticmethod
    def mark_neighbor_safe_of_monster(area, frontier):
        print("Mark safe")
        for neighbor in area.neighbors:
            if neighbor.received_cristal:
                print("is safe: ", neighbor.posX, neighbor.posY)
                InferenceEngine.add_to_frontier(neighbor, 0, frontier)

    @staticmethod
    def add_to_frontier(area, index, frontier):
        # If the area is already in the frontier at more risky range, we leave it there
        # except if it received a cristal
        for listindex, arealist in enumerate(frontier):
            if area in arealist:
                if listindex <= index:
                    arealist.remove(area)
                elif listindex > index and listindex == 1 and area.received_cristal():  # Case when we threw a cristal
                    arealist.remove(area)
                else:
                    return

        frontier[index].insert(0, area)

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
    def threw_stone_on_neighbor(area, frontier):
        for neighbor in area.neighbors:
            if neighbor.received_cristal():
                return True
        return False

    @staticmethod
    def agent_fell_in_neighbor(area, frontier):
        for neighbor in area.neighbors:
            if neighbor.user_fell_in:
                return True

    @staticmethod
    def agent_knows_hole_neighbor(area, frontier):
        print("Agent knows there is hole at")
        for neighbor in area.neighbors:
            if neighbor.user_fell_in:
                print(neighbor.posX, neighbor.posY)
                InferenceEngine.remove_from_frontier(neighbor, frontier)

    @staticmethod
    def remove_from_frontier(area, frontier):
        for arealist in frontier:
            if area in arealist:
               arealist.remove(area)

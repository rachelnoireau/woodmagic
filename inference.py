

class Inference:
    def __init__(self, premises, consequences):
        self.__was_executed = False
        self.__premises = premises
        self.__consequences = consequences

    def can_execute(self, context):
        for premise in self.__premises:
            # if not premise.is_known_true:
            if premise not in context:
                return False
        return True

    def execute(self):
        self.__was_executed = True
        return self.__consequences

    def get_premises(self):
        return self.__premises

    def get_consequences(self):
        return self.__consequences

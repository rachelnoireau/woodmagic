

class Inference:
    def __init__(self, premises, consequences):
        self.__was_executed = False
        self.__premises = premises
        self.__consequences = consequences

    def can_apply(self, context, *params):
        for premise in self.__premises:
            if not premise(context, params):
                return False
        return True

    def apply(self):
        self.__was_executed = True
        return self.__consequences

    def get_premises(self):
        return self.__premises

    def get_consequences(self):
        return self.__consequences

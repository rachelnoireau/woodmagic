

class Inference:
    def __init__(self, premises, consequences):
        self.was_executed = False
        self.premises = premises
        self.consequences = consequences

    def reset(self):
        self.was_executed = False

    def can_apply(self, context, params):
        if self.was_executed:
            return False
        for premise in self.premises:
            if not premise(context, params):
                return False
        return True

    def apply(self, context, params):
        self.was_executed = True
        for consequence in self.consequences:
            return consequence(context, params)

    def get_premises(self):
        return self.premises

    def get_consequences(self):
        return self.consequences

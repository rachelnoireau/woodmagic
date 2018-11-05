from area import Area
from wood import Wood
from display import Display

class Simulation:
    def __init__(self):
        self.size = 3

        self.wood = Wood(self.size)
        self.display = Display(self.size)

        self.display.add_grid(self.wood.get_grid())
        self.display.create_button()
        self.display.start_loop()



if __name__ == '__main__':
    Simulation()

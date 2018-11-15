
class Area:

	def __init__(self, posX, posY):
		self.posX = posX
		self.posY = posY
		self.was_visited = False
		
		self.is_monster = False
		self.is_hole = False
		self.is_next_to_monster = False
		self.is_next_to_hole = False
		self.is_portal = False
		self.is_cristal = False

		self.__risky_of_hole = False
		self.__risky_of_monster = False
		self.__received_stone = False

		self.neighbors = []
		self.right_neighbour = None
		self.left_neighbour = None
		self.up_neighbour = None
		self.down_neighbour = None

	def onNeighborsSet(self):
		self.neighbors = [self.left_neighbour, self.right_neighbour, self.up_neighbour, self.down_neighbour]
		self.neighbors = [n for n in self.neighbors if n is not None]

	def take_cristal(self):
		self.is_cristal = False
		
	def cristal_use(self):
		self.is_monster = False

		
	def set_monster(self):
		self.is_monster = True
		
	def set_hole(self):
		self.is_hole = True
	
	def set_next_to_monster(self):
		self.is_next_to_monster = True
		
	def set_next_to_hole(self):
		self.is_next_to_hole = True
		
	def set_portal(self):
		self.is_portal = True
		
	def set_cristal(self):
		self.is_cristal = True
		
	def kill_monster(self):
		self.is_monster = False




	def get_monster(self):
		return self.is_monster

	def get_hole(self):
		return self.is_hole

	def get_portal(self):
		return self.is_portal

	def get_is_next_to_monster(self):
		return self.is_next_to_monster

	def is_safe(self):
		return not (self.is_monster or self.is_hole)

	def mark_risky_of_hole(self):
		self.__risky_of_hole = True

	def is_risky_of_hole(self):
		return self.__risky_of_hole

	def mark_risky_of_monster(self):
		self.__risky_of_monster = True

	def is_risky_of_monster(self):
		return self.__risky_of_monster

	def receive_stone(self):
		self.__received_stone = True

	def received_stone(self):
		return self.__received_stone

	def mark_safe(self):
		self.__risky_of_wind = False
		self.__risky_of_monster = False

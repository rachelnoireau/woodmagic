
class Area:

	def __init__(self, posX, posY):
		self.posX = posX
		self.posY = posY
		
		self.is_monster = False
		self.is_hole = False
		self.is_next_to_monster = False
		self.is_next_to_hole = False
		self.is_portal = False
		self.is_cristal = False
		
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
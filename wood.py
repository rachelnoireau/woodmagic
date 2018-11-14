import random

from area import Area

class Wood:
	
	PROB_MONSTER = 0.09
	PROB_HOLE = 0.09
	PROB_CRISTAL = 0.05

	def __init__(self,size):
		self.perf = 0;
		self.size = size
		self.grid = [[Area(x, y) for x in range(self.size)] for y in range(self.size)]

		self.situate_portal()
		for i in range (0, self.size):
			for j in range (0, self.size):
				if not(self.grid[i][j].get_portal()):
					if not(self.generate_monster(i,j)):
						self.generate_hole(i,j)
				self.generate_cristal(i,j)
		
	
	def cristal_taken(self, posx,posy):
		self.grid[posx][posy].take_cristal()
		
	def use_cristal(self, posx, posy):
		self.grid[posx][posy].cristal_use()
		
	def get_grid(self):
		return self.grid
	
	def situate_portal(self):
		posx = random.randint(1,self.size-1)
		posy = random.randint(1,self.size-1)
		self.grid[posx][posy].set_portal()
		
	def generate_monster(self, posx, posy):
		if (random.random() < self.PROB_MONSTER):
			self.grid[posx][posy].set_monster()
			if(posx>0):
				self.grid[posx-1][posy].set_next_to_monster()
			if(posx<self.size-1):
				self.grid[posx+1][posy].set_next_to_monster()
			if(posy>0):
				self.grid[posx][posy-1].set_next_to_monster()
			if(posy<self.size-1):
				self.grid[posx][posy+1].set_next_to_monster()
			return True
		return False
				
	def generate_hole(self, posx, posy):
		if (random.random() < self.PROB_HOLE):
			self.grid[posx][posy].set_hole()
			if(posx>0):
				self.grid[posx-1][posy].set_next_to_hole()
			if(posx<self.size-1):
				self.grid[posx+1][posy].set_next_to_hole()
			if(posy>0):
				self.grid[posx][posy-1].set_next_to_hole()
			if(posy<self.size-1):
				self.grid[posx][posy+1].set_next_to_hole()

	def generate_cristal(self, posx, posy):
		if (random.random() < self.PROB_CRISTAL):
			self.grid[posx][posy].set_cristal()

	def performance(area,agent, self):
		if(area.is_monster == True or area.is_hole == True):
			self.perf = self.perf - 10 * self.size
		elif (area.is_portal == True):
			self.perf = self.perf + 10 * self.size
		elif (agent.action ==  'USE_CRISTAL'):
			self.perf = self.perf - 10
		else :
			self.perf = self.perf - 1
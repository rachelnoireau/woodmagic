import random

from area import Area


class Wood:
	
	PROB_MONSTER = 0.2
	PROB_HOLE = 0.2

	def __init__(self, size):
		self.perf = 0
		self.size = size
		self.grid = [[Area(x, y) for x in range(self.size)] for y in range(self.size)]

		self.situate_portal()
		for i in range (0, self.size):
			for j in range (0, self.size):
				self.grid[i][j].left_neighbour = self.get_area_at_position(j - 1, i)
				self.grid[i][j].right_neighbour = self.get_area_at_position(j + 1, i)
				self.grid[i][j].up_neighbour = self.get_area_at_position(j, i - 1)
				self.grid[i][j].down_neighbour = self.get_area_at_position(j, i + 1)
				self.grid[i][j].onNeighborsSet()
				if not(i == 0 & j == 0):
					if not(self.grid[i][j].get_portal()):
						if not(self.generate_monster(j,i)):
							self.generate_hole(j,i)

	def use_cristal(self, posx, posy):
		self.grid[posy][posx].cristal_use()
		
	def get_grid(self):
		return self.grid
	
	#give random position to portal
	def situate_portal(self):
		posx = random.randint(0, self.size-1)
		posy = random.randint(0, self.size-1)
		if( posx == 0 & posy == 0 ):
			self.situate_portal()
		else:
			self.grid[posy][posx].set_portal()
	
	#give random position to monster, 
	def generate_monster(self, posx, posy):
		if (random.random() < self.PROB_MONSTER):
			self.grid[posy][posx].set_monster()
			if(posy>0):
				self.grid[posy-1][posx].set_next_to_monster()
			if(posy<self.size-1):
				self.grid[posy+1][posx].set_next_to_monster()
			if(posx>0):
				self.grid[posy][posx-1].set_next_to_monster()
			if(posx<self.size-1):
				self.grid[posy][posx+1].set_next_to_monster()
			return True
		return False
	
	#give random position to hole, and put wind next to it 
	def generate_hole(self, posx, posy):
		if (random.random() < self.PROB_HOLE):
			self.grid[posy][posx].set_hole()
			if(posy>0):
				self.grid[posy-1][posx].set_next_to_hole()
			if(posy<self.size-1):
				self.grid[posy+1][posx].set_next_to_hole()
			if(posx>0):
				self.grid[posy][posx-1].set_next_to_hole()
			if(posx<self.size-1):
				self.grid[posy][posx+1].set_next_to_hole()
	
	#give a score to agent
	def performance(area,agent, self):
		if(area.is_monster == True or area.is_hole == True):
			self.perf = self.perf - 10 * self.size #the more grill is big the more it is difficulte to found the portal
		elif (area.is_portal == True):
			self.perf = self.perf + 10 * self.size
		elif (agent.action ==  'USE_CRISTAL'):
			self.perf = self.perf - 10 #lose a cristal
		else :
			self.perf = self.perf - 1 #it take time to find the portal

	def get_area_at_position(self, x, y):
		if x < 0 or x >= self.size or y < 0 or y >= self.size:
			return None
		return self.grid[y][x]

	def move_up(self):
		return None

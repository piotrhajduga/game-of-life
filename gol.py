class GameOfLife(object):
	def __init__(self, state):
		self.current_state = state
	
	def neighbour_count(self, x, y):
		number_of = 0
		if (x-1, y-1) in self.current_state: number_of += 1
		if (x-1, y) in self.current_state: number_of += 1
		if (x-1, y+1) in self.current_state: number_of += 1
		if (x, y-1) in self.current_state: number_of += 1
		if (x, y+1) in self.current_state: number_of += 1
		if (x+1, y-1) in self.current_state: number_of += 1
		if (x+1, y) in self.current_state: number_of += 1
		if (x+1, y+1) in self.current_state: number_of += 1
		return number_of

	def get_new_state(self, x, y):
		nc = self.neighbour_count(x, y)
		if (x,y) in self.current_state:
			return not (nc < 2 or nc > 3)
		elif nc==3:
			return True
		return False


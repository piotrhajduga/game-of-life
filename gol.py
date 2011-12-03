class GameOfLife(object):

    def __init__(self, state):
        self.current_state = state
    
    def neighbour_count(self, x, y):
        number_of = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if (i, j) == (x, y):
                    continue
                if (i, j) in self.current_state:
                    number_of += 1
        return number_of

    def get_new_state(self, x, y):
        nc = self.neighbour_count(x, y)
        if (x, y) in self.current_state:
            return  (nc in [2,3])
        elif nc == 3:
            return True
        return False

    def next_state(self):
        result = set()
        for (x, y) in self.current_state:
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if self.get_new_state(i, j):
                        result.add((i, j))
        self.current_state = result
        return result

def print_state(gol,start,end):
	for i in range(start[0],end[0]+1):
		line = ""
		for j in range(start[1],end[1]+1):
			if (i,j) in gol.current_state:
				line += '#'
			else:
				line += ' '
		print(line)

if __name__ == '__main__':
	gol = GameOfLife(set([(0,2),(1,2),(1,3),(2,3)]))
	print('-1:\n')
	print_state(gol,(-1,-1),(5,5))
	for i in range(4):
		print('%d:\n' % i)
		gol.next_state()
		print_state(gol,(-1,-1),(5,5))

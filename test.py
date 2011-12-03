import unittest
from gol import GameOfLife

class Test(unittest.TestCase):
	def setUp(self):
		self.gol = GameOfLife(set([(1,1),(1,2),(1,3),(2,3)]))
	
	def testNeighbourCount(self):
		self.assertEquals(1,self.gol.neighbour_count(1,1))

	def testGetNewStateDie(self):
		assert(self.gol.get_new_state(1,1)==False)

	def testGetNewStateStayAlive(self):
		assert(self.gol.get_new_state(1,2))

	def testGetNewStateBreed(self):
		assert(self.gol.get_new_state(0,2))

	def testGetNewStateBreed(self):
		assert(self.gol.get_new_state(2,2)==False)
	
	def testNextState(self):
		expected = set([(0,2),(1,2),(1,3),(2,3)])
		self.assertEquals(expected,self.gol.next_state())

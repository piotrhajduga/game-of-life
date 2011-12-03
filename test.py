import unittest
from gol import GameOfLife

class Test(unittest.TestCase):
	def setUp(self):
		self.gol = GameOfLife(set([(1,1),(1,2),(1,3),(2,3)]))
	
	def testNeighbourCount(self):
		self.assertEquals(1,self.gol.neighbour_count(1,1))


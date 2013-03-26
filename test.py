import unittest
from gol import GameOfLife


class Test(unittest.TestCase):
    def setUp(self):
        self.gol = GameOfLife(
            set([(1, 1), (1, 2), (1, 3), (2, 3)])
        )

    def test_neighbour_count(self):
        self.assertEqual(1, self.gol.get_neighbour_count(1, 1))

    def test_get_new_state_die(self):
        self.assertFalse(self.gol.get_new_state(1, 1))

    def test_get_new_state_stay_alive(self):
        self.assertTrue(self.gol.get_new_state(1, 2))

    def test_get_new_state_breed(self):
        self.assertTrue(self.gol.get_new_state(0, 2))
        self.assertFalse(self.gol.get_new_state(2, 2))

    def test_next_state(self):
        expected = set([(0, 2), (1, 2), (1, 3), (2, 3)])
        generations_count = self.gol.generations_count
        self.assertEqual(expected, self.gol.next_state())
        self.assertEqual(generations_count + 1, self.gol.generations_count)

    def test_set_state(self):
        expected = set([(1, 2), (-2, 0), (0, 0)])
        self.gol.set_state(expected)
        self.assertEqual(expected, self.gol.current_state)
        self.assertEqual(0, self.gol.generations_count)

import unittest
from conway import *
__author__ = 'Roland'

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_alive_cell(self):
        self.assertEquals(False, next_state(True, 1))
        self.assertEquals(True, next_state(True, 2))
        self.assertEquals(True, next_state(True, 3))
        self.assertEquals(False, next_state(True, 4))
        self.assertEquals(False, next_state(True, 5))

    def test_dead_cell(self):
        self.assertEquals(False, next_state(False, 1))
        self.assertEquals(False, next_state(False, 2))
        self.assertEquals(True, next_state(False, 3))
        self.assertEquals(False, next_state(False, 4))
        self.assertEquals(False, next_state(False, 5))


    def test_countNeighbours_singleCell_has0neighbours(self):
        universe = {(0, 0)}
        cell = (0, 0)
        self.assertEquals(0, countNeighbours(universe, cell))

    def test_countNeighbours_two_distant_cells_have0neighbours(self):
        universe = {(0,0), (100,100)}
        self.assertEquals(0, countNeighbours(universe, (100, 100)))
        self.assertEquals(0, countNeighbours(universe, (0,0)))

    def test_countNeighbourse_two_adjacent_cells_have1neighbour(self):
        universe = {(0,0), (0, 1)}
        self.assertEquals(1, countNeighbours(universe, (0, 0)))
        self.assertEquals(1, countNeighbours(universe, (0, 1)))

    def test_countNeighbours_diagonal_cells_have_1_neighbour(self):
        universe = {(0,0), (1, 1)}
        self.assertEquals(1, countNeighbours(universe, (0, 0)))
        self.assertEquals(1, countNeighbours(universe, (1, 1)))

    def test_countNeighbours_4_conglomerate_cells_have_3_neighbours_each(self):
        universe = {(0, 0), (1, 1), (1, 0), (0, 1)}
        self.assertEquals(3, countNeighbours(universe, (0, 0)))
        self.assertEquals(3, countNeighbours(universe, (1, 1)))
        self.assertEquals(3, countNeighbours(universe, (0, 1)))
        self.assertEquals(3, countNeighbours(universe, (1, 0)))

    def test_neighboring_cells_are_neighbours(self):
        self.assertTrue(areNeighbours((1,1), (1,0)))
        self.assertTrue(areNeighbours((1,1), (0,0)))
        self.assertTrue(areNeighbours((1,1), (0,1)))

    def test_not_neighboring_cell_are_not_neighbors(self):
        self.assertFalse(areNeighbours((0,1), (100, 100)))
        self.assertFalse(areNeighbours((0,1), (1, 3)))
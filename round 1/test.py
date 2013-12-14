from conway import *
import unittest

__author__ = 'Roland'


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_two_cells_die(self):
        cells = {(0, 0), (0, 1)}
        next_cells = tick(cells)
        self.assertSetEqual(next_cells, set())

    def test_three_cells_live(self):
        cells = {(0, 0), (0, 1), (1,1)}
        next_cells = tick(cells)
        self.assertSetEqual(next_cells, {(0, 0), (0, 1), (1,1), (1,0)})

    def test_four_neighbors_die(self):
        cells = {(0,0), (0,1), (1,1), (1,0), (-1,1)}
        next_cells = tick(cells)
        self.assertSetEqual(next_cells, {(1, 0), (1,1), (-1,1), (0, 2), (-1, 0)})


    def test_neighborhood_count(self):
        cells = {(0,0) ,(1,1), (2,2), (3,1), (4,1), (4, 0), (3, 3), (3, 4), (4,3), (4,4) }
        self.assertEquals(1, neighbor_count((0,0), cells))
        self.assertEquals(2, neighbor_count((1,1), cells))
        self.assertEquals(3, neighbor_count((2,2), cells))
        self.assertEquals(3, neighbor_count((3,1), cells))
        self.assertEquals(4, neighbor_count((3,3), cells))
        self.assertEquals(0, neighbor_count((100,100), cells))
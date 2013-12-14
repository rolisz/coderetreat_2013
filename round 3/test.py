import unittest
from conway import *

__author__ = 'Roland'

class Provider(object):

    def max_nr_neighbors(self):
        return 8

class Test3(unittest.TestCase):

    def buildCell(self):
        return Cell(Provider())

    def test_new_cell_has_empty_neighbor_list(self):
        c = self.buildCell()
        self.assertEquals([], c.neighbors)

    def test_new_cell_add_neighbor_has_neighbor(self):
        c = self.buildCell()
        c2 = self.buildCell()
        c.addNeighbor(c2)

        self.assertEquals([c2], c.neighbors)

    def test_new_cell_add_multiple_neighbors(self):
        c = self.buildCell()

        c.addNeighbor(self.buildCell(), self.buildCell())

        self.assertEqual(2, len(c.neighbors))

    def test_cell_with_no_neighbors_dies(self):
        c = self.buildCell()

        self.assertEquals(None, c.tick())

    def test_cell_with_two_neighbors_lives(self):
        c = self.buildCell()

        c.addNeighbor(self.buildCell(), self.buildCell())

        self.assertEquals(c, c.tick())

    def test_cell_with_three_neighbors_lives(self):
        c = self.buildCell()

        c.addNeighbor(self.buildCell(), self.buildCell(), self.buildCell())

        self.assertEquals(c, c.tick())

    def test_cell_dies_of_overpopulation(self):
        c = self.buildCell()

        c.addNeighbor(*[self.buildCell() for _ in range(4)])

        self.assertEquals(None, c.tick())

    def test_cell_with_8_dies(self):
        c = self.buildCell()

        c.addNeighbor(*[self.buildCell() for _ in range(8)])

        self.assertEquals(None, c.tick())

    def test_cell_cant_have_more_than_8_neighbors(self):
        c = self.buildCell()

        c.addNeighbor(*[self.buildCell() for _ in range(8)])

        try:
            c.addNeighbor(self.buildCell())
            self.assertTrue(False)
        except CellException:
            self.assertTrue(True)
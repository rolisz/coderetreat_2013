from conway import tick
import unittest

__author__ = 'Roland'


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_two_cells_die(self):
        cells = [(0,0), (0,1)]
        next_cells = tick(cells)
        self.assertListEqual(next_cells, [])
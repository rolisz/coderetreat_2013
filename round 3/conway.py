__author__ = 'Roland'

class Cell(object):

    def __init__(self, provider):
        self.provider = provider
        self.neighbors = []

    def addNeighbor(self, *args):
        if len(self.neighbors) == self.provider.max_nr_neighbors():
            raise CellException("Too many neighbors")
        self.neighbors.extend(args)

    def tick(self):
        if 2 <= len(self.neighbors) <= 3:
            return self

class CellException(Exception):
    pass


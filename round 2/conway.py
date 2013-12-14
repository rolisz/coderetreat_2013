__author__ = 'Roland'

def next_state(alive, nrNeighbours):
    if alive :
        if nrNeighbours < 2:
            return False
        elif nrNeighbours <= 3:
            return True
        else:
            return False
    else:
        if nrNeighbours == 3:
            return True
        else:
            return False

def countNeighbours(universe, cell):
    neighbours = 0
    for c in universe:
        if c != cell and areNeighbours(c, cell):
            neighbours += 1

    return neighbours

def areNeighbours(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    if abs(x1 - x2) == 1 or abs(y1 - y2) == 1:
        return True
    else:
        return False
from time import sleep

__author__ = 'Roland'


def neighbor_count(cell, cells):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            neighbor_cell = (cell[0] + i, cell[1] + j)
            if neighbor_cell != cell and neighbor_cell in cells:
                count += 1
    return count


def stays_alive(cell, cells):
    nr_neighbors = neighbor_count(cell, cells)
    if 2 <= nr_neighbors <= 3:
        return True
    return False


def resurect(candidates, cells):
    resurects = set()
    for candidate in candidates:
        if neighbor_count(candidate, cells) == 3:
            resurects.add(candidate)

    return resurects


def tick(cells):
    new_cells = set()

    for cell in cells:
        if stays_alive(cell, cells):
            new_cells.add(cell)

    candidates = set()

    for cell in cells:
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbor_cell = (cell[0] + i, cell[1] + j)
                if neighbor_cell not in cells:
                    candidates.add(neighbor_cell)

    new_cells.update(resurect(candidates, cells))

    return new_cells


def show_universe(cells):
    min_x = min(map(lambda x: x[0], cells))
    max_x = max(map(lambda x: x[0], cells))
    min_y = min(map(lambda x: x[1], cells))
    max_y = max(map(lambda x: x[1], cells))

    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            print(" X " if (i, j) in cells else "   ", end="")

        print("\n")

cells = {(0,0) ,(1,1), (2,2), (3,1), (4,1), (4, 0), (3, 3), (3, 4), (4,3), (4,4) }

while True:
    show_universe(cells)
    sleep(1)
    cells =tick(cells)
    print("===========")
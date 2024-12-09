import unittest

def node_locations(grid):
    nodes = dict()
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if cell != ".":
                nodes[cell] = nodes[cell] if cell in nodes else []
                nodes[cell].append((x, y))
    return nodes

def anti_nodes_locations_1(grid, coords): 
    max_x, max_y = len(grid[0]), len(grid)
    pairs = [(a, b) for idx, a in enumerate(coords) for b in coords[idx + 1:]]
    anti_nodes = set()
    for a, b in pairs:
        dx, dy = b[0] - a[0], b[1] - a[1]
        anti_node_1 = (a[0] - dx, a[1] - dy)
        anti_node_2 = (b[0] + dx, b[1] + dy) 
        if anti_node_1[0] >= 0 and anti_node_1[0] < max_x and anti_node_1[1] >= 0 and anti_node_1[1] < max_y:
            anti_nodes.add(anti_node_1)
        if anti_node_2[0] >= 0 and anti_node_2[0] < max_x and anti_node_2[1] >= 0 and anti_node_2[1] < max_y:
            anti_nodes.add(anti_node_2)
    return anti_nodes

def anti_nodes_locations_2(grid, coords): 
    max_x, max_y = len(grid[0]), len(grid)
    pairs = [(a, b) for idx, a in enumerate(coords) for b in coords[idx + 1:]]
    anti_nodes = set()
    for a, b in pairs:
        anti_nodes.add(a)
        anti_nodes.add(b)
        dx, dy = b[0] - a[0], b[1] - a[1]
        anti_node_1 = (a[0] - dx, a[1] - dy)
        anti_node_2 = (b[0] + dx, b[1] + dy) 
        while anti_node_1[0] >= 0 and anti_node_1[0] < max_x and anti_node_1[1] >= 0 and anti_node_1[1] < max_y:
            anti_nodes.add(anti_node_1)
            anti_node_1 = (anti_node_1[0] - dx, anti_node_1[1] - dy)
        while anti_node_2[0] >= 0 and anti_node_2[0] < max_x and anti_node_2[1] >= 0 and anti_node_2[1] < max_y:
            anti_nodes.add(anti_node_2)
            anti_node_2 = (anti_node_2[0] + dx, anti_node_2[1] + dy) 
    return anti_nodes

def solve_1(input):
    grid = [list(line) for line in input.split("\n")]
    nodes = node_locations(grid)
    anti_nodes = set()
    for coords in nodes.values():
        anti_nodes |= anti_nodes_locations_1(grid, coords)
    return len(anti_nodes)

def solve_2(input):
    grid = [list(line) for line in input.split("\n")]
    nodes = node_locations(grid)
    anti_nodes = set()
    for coords in nodes.values():
        anti_nodes |= anti_nodes_locations_2(grid, coords)
    return len(anti_nodes)

with open("./input.txt") as f:
    input = f.read()

with open("./example.txt") as f:
    example = f.read()

class Test(unittest.TestCase):
    def test_solve_example_1(self):
        self.assertEqual(solve_1(example), 14)

    def test_solve_1(self):
        self.assertEqual(solve_1(input), 308)

    def test_solve_example_2(self):
        self.assertEqual(solve_2(example), 34)

    def test_solve_2(self):
        self.assertEqual(solve_2(input), 1147)

unittest.main()

import unittest

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def find_trailheads(grid):
    return [(x, y) for y, row in enumerate(grid) for x, cell in enumerate(row) if cell == 0]

def check_trail(grid, x, y, new_x, new_y):
    return 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_y][new_x] == grid[y][x] + 1

def traverse(grid, x, y, nines):
    if grid[y][x] == 9: return set([(x, y)])
    for dx, dy in DIRS:
        new_x, new_y = x + dx, y + dy
        if check_trail(grid, x, y, new_x, new_y):
            nines |= traverse(grid, new_x, new_y, nines)
    return nines

def traverse_2(grid, x, y, count):
    if grid[y][x] == 9: return count + 1
    for dx, dy in DIRS:
        new_x, new_y = x + dx, y + dy
        if check_trail(grid, x, y, new_x, new_y):
            count = traverse_2(grid, new_x, new_y, count)
    return count

def solve_1(input):
    grid = [list(map(int, list(line))) for line in input.split("\n")]
    trailheads = find_trailheads(grid)
    return sum([len(traverse(grid, x, y, set())) for x, y in trailheads])

def solve_2(input):
    grid = [list(map(int, list(line))) for line in input.split("\n")]
    trailheads = find_trailheads(grid)
    return sum([traverse_2(grid, x, y, 0) for x, y in trailheads])

with open("./example.txt")  as f: example  = f.read()
with open("./example2.txt") as f: example2 = f.read()
with open("./input.txt")    as f: input    = f.read()

class Test(unittest.TestCase):
    def test_solve_example_1(self):
        self.assertEqual(solve_1(example), 1)

    def test_solve_example_1_2(self):
        self.assertEqual(solve_1(example2), 36)

    def test_solve_1(self):
        self.assertEqual(solve_1(input), 688)

    def test_solve_example_2(self):
        self.assertEqual(solve_2(example2), 81)

    def test_solve_2(self):
        self.assertEqual(solve_2(input), 1459)

unittest.main()

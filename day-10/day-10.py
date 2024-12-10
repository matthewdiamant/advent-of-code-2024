import unittest

def traverse(grid, x, y, counter, add):
    if grid[y][x] == 9: return add((x, y), counter)
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_y][new_x] == grid[y][x] + 1:
            counter = traverse(grid, new_x, new_y, counter, add)
    return counter

def solve(input, counter, add, len):
    grid = [list(map(int, list(line))) for line in input.split("\n")]
    trailheads = [(x, y) for y, row in enumerate(grid) for x, cell in enumerate(row) if cell == 0]
    return sum([len(traverse(grid, x, y, counter, add)) for x, y in trailheads])

def union(position, value): return set([position]) | value
def set_len(s): return len(s)
def add(_, value): return value + 1
def int_len(s): return s

with open("./example.txt")  as f: example  = f.read()
with open("./example2.txt") as f: example2 = f.read()
with open("./input.txt")    as f: input    = f.read()

class Test(unittest.TestCase):
    def test_solve_example_1(self):
        self.assertEqual(solve(example, set(), union, set_len), 1)

    def test_solve_example_1_2(self):
        self.assertEqual(solve(example2, set(), union, set_len), 36)

    def test_solve_1(self):
        self.assertEqual(solve(input, set(), union, set_len), 688)

    def test_solve_example_2(self):
        self.assertEqual(solve(example2, 0, add, int_len), 81)

    def test_solve_2(self):
        self.assertEqual(solve(input, 0, add, int_len), 1459)

unittest.main()

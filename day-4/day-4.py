import unittest

def solve_1(input):
    count = 0
    grid = [list(line) for line in input.split("\n")]
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "X":
                # check all 8 directions
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if y + dy * 3 < 0 or y + dy * 3 >= len(grid):
                            continue
                        if x + dx * 3 < 0 or x + dx * 3 >= len(row):
                            continue
                        if grid[y + dy][x + dx] == "M" and grid[y + dy * 2][x + dx * 2] == "A" and grid[y + dy * 3][x + dx * 3] == "S":
                            count += 1
    return count

def solve_2(input):
    count = 0
    grid = [list(line) for line in input.split("\n")]
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "A":
                if y - 1 < 0 or y + 1 >= len(grid):
                    continue
                if x - 1 < 0 or x + 1 >= len(row):
                    continue
                if ((grid[y - 1][x - 1] == "M" and grid[y + 1][x + 1] == "S") or \
                    (grid[y - 1][x - 1] == "S" and grid[y + 1][x + 1] == "M")
                ) and \
                ((grid[y - 1][x + 1] == "M" and grid[y + 1][x - 1] == "S") or \
                    (grid[y - 1][x + 1] == "S" and grid[y + 1][x - 1] == "M")
                ):
                    count += 1
    return count

with open("./input.txt") as f:
    input = f.read()

with open("./example.txt") as f:
    example = f.read()

with open("./example2.txt") as f:
    example2 = f.read()

class Test(unittest.TestCase):
    def test_solve_example_1(self):
        self.assertEqual(solve_1(example), 4)

    def test_solve_example_2(self):
        self.assertEqual(solve_1(example2), 18)

    def test_solve_1(self):
        self.assertEqual(solve_1(input), 2504)

    def test_solve_example_2_1(self):
        self.assertEqual(solve_2(example2), 9)

    def test_solve_2_1(self):
        self.assertEqual(solve_2(input), 1923)

unittest.main()

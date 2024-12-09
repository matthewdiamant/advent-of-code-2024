import unittest

def find_guard(grid):
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if cell == "^":
                return { "x": x, "y": y }

def get_visited(grid):
    guard = find_guard(grid)
    dx, dy = 0, -1
    visited = set([(guard["x"], guard["y"])])
    while guard["y"] + dy >= 0 and guard["y"] + dy < len(grid) and guard["x"] + dx >= 0 and guard["x"] + dx < len(grid[0]):
        if grid[guard["y"] + dy][guard["x"] + dx] == "#":
            new_dx, new_dy = dy * -1, dx
            dx, dy = new_dx, new_dy
        else:
            guard["x"] += dx
            guard["y"] += dy
            visited.add((guard["x"], guard["y"]))
    return visited

def solve_1(input):
    grid = [list(line) for line in input.split("\n")]
    return len(get_visited(grid))

def is_obstruction_loop_causing(grid, guard):
    dx, dy = 0, -1
    visited = set()
    while guard["y"] + dy >= 0 and guard["y"] + dy < len(grid) and guard["x"] + dx >= 0 and guard["x"] + dx < len(grid[0]):
        if grid[guard["y"] + dy][guard["x"] + dx] == "#":
            new_dx, new_dy = dy * -1, dx
            dx, dy = new_dx, new_dy
        else:
            guard["x"] += dx
            guard["y"] += dy
            if (guard["x"], guard["y"], dx, dy) in visited:
                return True
            visited.add((guard["x"], guard["y"], dx, dy))
    return False

def solve_2(input):
    grid = [list(line) for line in input.split("\n")]
    guard = find_guard(grid)
    visited = get_visited(grid)
    obstruction_count = 0
    for x, y in visited:
        test_grid = [line.copy() for line in grid]
        test_grid[y][x] = "#"
        if is_obstruction_loop_causing(test_grid, guard.copy()):
            obstruction_count += 1
    return obstruction_count

with open("./input.txt") as f:
    input = f.read()

with open("./example.txt") as f:
    example = f.read()

class Test(unittest.TestCase):
    def test_solve_example_1(self):
        self.assertEqual(solve_1(example), 41)

    def test_solve_1(self):
        self.assertEqual(solve_1(input), 5531)

    def test_solve_example_2(self):
        self.assertEqual(solve_2(example), 6)

    def test_solve_2(self):
        self.assertEqual(solve_2(input), 2165)

unittest.main()

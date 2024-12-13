import unittest
from functools import cache

def change(node):
    if node == 0:
        return[1]
    elif len(str(node)) % 2 == 0:
        length = len(str(node))
        return [int(str(node)[:length // 2]), int(str(node)[length // 2:])]
    else:
        return [node * 2024]

@cache
def blink(node, steps):
    if steps == 0: return 1
    new_stones = change(node)
    return sum([blink(new_stone, steps - 1) for new_stone in new_stones])

def solve(input, steps):
    stones = [int(value) for value in input.split(" ")]
    return sum([blink(stone, steps) for stone in stones])

with open("./example.txt") as f: example = f.read()
with open("./input.txt")   as f: input   = f.read()

class Test(unittest.TestCase):
    def test_solve_example_1(self):
        self.assertEqual(solve(example, 25), 55312)

    def test_solve_1(self):
        self.assertEqual(solve(input, 25), 193607)

    def test_solve_2(self):
        self.assertEqual(solve(input, 75), 229557103025807)

unittest.main()

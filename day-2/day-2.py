import unittest
from pprint import pprint


def get_reports(input):
    return [[int(level) for level in line.split()] for line in input.split("\n") if line]

def tolerant_is_safe(level):
    for i in range(len(level)):
        copy = level.copy()
        copy.pop(i)
        if (is_safe(copy)):
            return 1
    return 0

def is_safe(level):
    if (level[0] > level[1]):
        level.reverse()
    for i in range(len(level)):
        if i != 0:
            difference = level[i] - level[i - 1]
            if (difference < 1 or difference > 3):
                return 0
    return 1

def solve_1(input):
    reports = get_reports(input)
    return sum([is_safe(level) for level in reports])

def solve_2(input):
    reports = get_reports(input)
    return sum([tolerant_is_safe(level) for level in reports])

with open("./input.txt") as f:
    input = f.read()

with open("./example.txt") as f:
    example = f.read()

class Test(unittest.TestCase):
    def test_solve_example_1(self):
        self.assertEqual(solve_1(example), 2)

    def test_solve_1(self):
        self.assertEqual(solve_1(input), 369)

    def test_solve_example_2(self):
        self.assertEqual(solve_2(example), 4)

    def test_solve_2(self):
        self.assertEqual(solve_2(input), 428)

unittest.main()

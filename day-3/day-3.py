import unittest
import re

def solve_1(input):
    muls = re.findall(r"mul\(\d+,\d+\)", input)
    operands = [map(int, re.findall(r"\d+", mul)) for mul in muls]
    return sum([a * b for a, b in operands])

def solve_2(input):
    [do_input, *donts] = input.split("don't()")
    for dont in donts:
        do_input += ''.join(dont.split("do()")[1:])
    return solve_1(do_input)

with open("./input.txt") as f:
    input = f.read()

with open("./example.txt") as f:
    example = f.read()

with open("./example2.txt") as f:
    example2 = f.read()

class Test(unittest.TestCase):
    def test_solve_example_1(self):
        self.assertEqual(solve_1(example), 161)

    def test_solve_1(self):
        self.assertEqual(solve_1(input), 179834255)

    def test_solve_example_2(self):
        self.assertEqual(solve_2(example2), 48)

    def test_solve_2(self):
        self.assertEqual(solve_2(input), 80570939)

unittest.main()

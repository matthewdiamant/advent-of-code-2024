import unittest

def parse_input(input):
    firsts = sorted([x.split()[0] for x in input.split("\n") if x])
    seconds = sorted([x.split()[1] for x in input.split("\n") if x])
    return [firsts, seconds]

def solve_1(input):
    [firsts, seconds] = parse_input(input)
    return sum([abs(int(first) - int(seconds[index])) for index, first in enumerate(firsts)])

def solve_2(input):
    [firsts, seconds] = parse_input(input)
    return sum([int(first) * seconds.count(first) for first in firsts])

with open("./input.txt") as f:
    input = f.read()

with open("./example.txt") as f:
    example = f.read()

class Test(unittest.TestCase):
    def test_solve_example_1(self):
        self.assertEqual(solve_1(example), 11)

    def test_solve_1(self):
        self.assertEqual(solve_1(input), 2756096)

    def test_solve_example_2(self):
        self.assertEqual(solve_2(example), 31)

    def test_solve_2(self):
        self.assertEqual(solve_2(input), 23117829)

unittest.main()

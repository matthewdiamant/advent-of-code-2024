import unittest
from operator import add, mul

def parse_line(line):
    value, operands = line.split(": ")
    return int(value), list(map(int, operands.split(" ")))

def is_valid(value, operands, funcs):
    answers = [operands[0]]
    for operand in operands[1:]:
        answers = [func(answer, operand) for func in funcs for answer in answers]
    return value in answers

def solve_1(input):
    lines = [parse_line(line) for line in input.split("\n")]
    funcs = [add, mul]
    return sum([value for value, operands in lines if is_valid(value, operands, funcs)])

def solve_2(input):
    lines = [parse_line(line) for line in input.split("\n")]
    funcs = [add, mul, lambda x, y: int(str(x) + str(y))]
    return sum([value for value, operands in lines if is_valid(value, operands, funcs)])

with open("./input.txt") as f:
    input = f.read()

with open("./example.txt") as f:
    example = f.read()

class Test(unittest.TestCase):
    def test_solve_example_1(self):
        self.assertEqual(solve_1(example), 3749)
        return

    def test_solve_1(self):
        self.assertEqual(solve_1(input), 5540634308362)

    def test_solve_example_2(self):
        self.assertEqual(solve_2(example), 11387)

    def test_solve_2(self):
        self.assertEqual(solve_2(input), 472290821152397)

unittest.main()

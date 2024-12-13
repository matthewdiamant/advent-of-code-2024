import unittest

def parse_line(s, delimiter):
    return [int(s.split(delimiter)[1].split(",")[0]), int(s.split(delimiter)[2].split(",")[0])]

def parse_input(input):
    machines = [lines.split("\n") for lines in input.split("\n\n")]
    return [(parse_line(a, "+"), parse_line(b, "+"), parse_line(c, "=")) for a, b, c in machines]

def solve_machine(machine, delta):
    button_a, button_b, prize = machine
    ax, ay = button_a
    bx, by = button_b
    px, py = prize
    px, py = px + delta, py + delta
    a = (py * bx - by * px) / (bx * ay - by * ax)
    b = (py - a * ay) / by
    if not a.is_integer() or not b.is_integer(): return 0
    return a * 3 + b * 1

def solve(input, delta):
    machines = parse_input(input)
    return int(sum([solve_machine(machine, delta) for machine in machines]))

with open("./example.txt") as f: example = f.read()
with open("./input.txt")   as f: input   = f.read()

class Test(unittest.TestCase):
    def test_solve_example_1(self):
        self.assertEqual(solve(example, 0), 480)

    def test_solve_1(self):
        self.assertEqual(solve(input, 0), 35729)

    def test_solve_2(self):
        self.assertEqual(solve(input, 10000000000000), 88584689879723)

unittest.main()

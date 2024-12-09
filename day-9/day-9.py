import unittest

def get_disk(input):
    disk = []
    id = 0
    for i, digit in enumerate(list(input)):
        disk += [(id if i % 2 == 0 else ".")] * int(digit)
        id += 1 if i % 2 == 0 else 0
    return disk

def get_disk_2(input):
    disk = []
    id = 0
    for i, digit in enumerate(list(input)):
        disk.append({ "id": id if i % 2 == 0 else  ".", "length": int(digit) })
        id += 1 if i % 2 == 0 else 0
    return disk

def get_compressed_disk(disk):
    empty = 0
    value = len(disk) - 1
    while disk[empty] != ".": empty += 1
    while disk[value] == ".": value -= 1
    while empty < value:
        disk[empty], disk[value] = disk[value], "."
        while disk[empty] != "." and empty != len(disk): empty += 1
        while disk[value] == "." and value != 0: value -= 1
    return disk

def get_compressed_disk_2(disk):
    value = len(disk) - 1
    while disk[value]["id"] == ".": value -= 1
    while value != 0:
        empty = 0
        while not (disk[empty]["id"] == "." and disk[empty]["length"] >= disk[value]["length"]) and empty != value:
            empty += 1
        if empty != value:
            new_disk = disk[:empty] + [disk[value]]
            if (disk[empty]["length"] - disk[value]["length"]) > 0:
                new_disk += [{ "id": ".", "length": disk[empty]["length"] - disk[value]["length"] }]
            new_disk += disk[empty + 1:value] + [{ "id": ".", "length": disk[value]["length"] }] + disk[value + 1:]
            disk = new_disk
        value -= 1
        while disk[value]["id"] == ".": value -= 1
    return flatten([[cell["id"]] * cell["length"] for cell in disk])

def flatten(xss):
    return [x for xs in xss for x in xs]

def get_checksum(disk):
    return sum([int(cell) * index for index, cell in enumerate(disk) if cell != "."])

def solve_1(input):
    disk = get_disk(input)
    compressed_disk = get_compressed_disk(disk)
    return get_checksum(compressed_disk)

def solve_2(input):
    disk = get_disk_2(input)
    compressed_disk = get_compressed_disk_2(disk)
    return get_checksum(compressed_disk)

with open("./input.txt") as f:
    input = f.read()

with open("./example.txt") as f:
    example = f.read()

with open("./example2.txt") as f:
    example2 = f.read()

class Test(unittest.TestCase):
    def test_solve_example_1_2(self):
        self.assertEqual(solve_1(example2), 60)

    def test_solve_example_1_1(self):
        self.assertEqual(solve_1(example), 1928)

    def test_solve_1(self):
        self.assertEqual(solve_1(input), 6390180901651)

    def test_solve_example_2(self):
        self.assertEqual(solve_2(example), 2858)

    def test_solve_2(self):
        self.assertEqual(solve_2(input), 6412390114238)

unittest.main()

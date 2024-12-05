import unittest

def parse_rules(rules):
    rules_dict = dict()
    for n, m in rules:
        rules_dict[n] = rules_dict[n] if n in rules_dict else []
        rules_dict[n].append(m)
    return rules_dict

def parse_input(input):
    rules, updates = input.split("\n\n")
    rules = parse_rules([rule.split("|") for rule in rules.split("\n")])
    updates = [update.split(",") for update in updates.split("\n")]
    return rules, updates

def validate_update(rules, update):
    for n, page in enumerate(update):
        for candidate_page in update[(n + 1):]:
            if candidate_page in rules and page in rules[candidate_page]:
                return False
    return True

def swap_pages(rules, update):
    for n, page in enumerate(update):
        for m, candidate_page in enumerate(update[(n + 1):]):
            if candidate_page in rules and page in rules[candidate_page]:
                update[n] = candidate_page
                update[n + 1 + m] = page
                return update


def fix_update(rules, update):
    while not validate_update(rules, update):
        update = swap_pages(rules, update)
    return update

def middle_pages(updates):
    return [int(update[len(update) // 2]) for update in updates]

def solve_1(input):
    rules, updates = parse_input(input)
    valid_updates = [update for update in updates if validate_update(rules, update)]
    return sum(middle_pages(valid_updates))

def solve_2(input):
    rules, updates = parse_input(input)
    invalid_updates = [fix_update(rules, update) for update in updates if not validate_update(rules, update)]
    return sum(middle_pages(invalid_updates))

with open("./input.txt") as f:
    input = f.read()

with open("./example.txt") as f:
    example = f.read()

class Test(unittest.TestCase):
    def test_solve_example_1(self):
        self.assertEqual(solve_1(example), 143)

    def test_solve_1(self):
        self.assertEqual(solve_1(input), 5087)

    def test_solve_example_2(self):
        self.assertEqual(solve_2(example), 123)

    def test_solve_2(self):
        self.assertEqual(solve_2(input), 4971)

unittest.main()

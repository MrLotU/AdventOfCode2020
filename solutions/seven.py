import re
import functools

TEST_INPUT = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''

with open(f'inputs/seven.txt', 'r') as f:
    _bags = f.read().split('\n')
    # _bags = TEST_INPUT.split('\n')

PATTERN = re.compile(r'(\d) ([a-z ]+) bag.*')


def parse_input(bags):
    _out = []
    for bag in bags:
        name, subs = bag.split(' bags contain ')
        _subBags = subs.split(', ')
        subBags = [PATTERN.match(sub).groups()
                   for sub in _subBags if PATTERN.match(sub) is not None]
        _out.append((name, subBags))

    return _out


class Bag:
    def __init__(self, name):
        self.name = name
        self.nodes = []

    @property
    def size(self):
        return len(self.nodes)

    def addNode(self, t):
        self.nodes.append(t)

    def nodeAt(self, i):
        return self.nodes[i][0]

    def numAt(self, i):
        return int(self.nodes[i][1])

print('---- DAY SEVEN PART ONE ----')

bags = parse_input(_bags)
tree = {n: Bag(n) for n, _ in bags}

for n, sub in bags:
    b = tree[n]
    for count, s in sub:
        subBag = tree[s]
        b.addNode((subBag, count))

def bag_connects_to(f: Bag, to):
    if f.name == to:
        return True
    for i in range(f.size):
        if bag_connects_to(f.nodeAt(i), to):
            return True
    return False

def find_num_conntected_to(bag):
    n = 0
    for node in tree.values():
        if bag_connects_to(node, bag):
            n += 1
        
    
    return n - 1


print(find_num_conntected_to('shiny gold'))

print('---- DAY SEVEN PART TWO ----')

def number_of_sub_bags(bag: Bag):
    if bag.size == 0:
        return 0
    size = 0
    for i in range(bag.size):
        n = bag.nodeAt(i)
        size += (bag.numAt(i) * number_of_sub_bags(n)) + bag.numAt(i)
    return size

print(number_of_sub_bags(tree['shiny gold']))
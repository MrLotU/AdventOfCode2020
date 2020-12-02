import re
from dataclasses import dataclass

TEST_IN = '''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc'''

with open(f'inputs/two.txt', 'r') as f:
    base_lines = f.read().split('\n')

PATTERN = re.compile(
    r'(?P<range_l>\d+)-(?P<range_u>\d+) (?P<letter>[a-z]): (?P<password>[a-z]+)')

@dataclass
class Line:
    range_l: int
    range_u: int
    letter: str
    password: str

    def validate(self):
        amount = self.password.count(self.letter)
        r = range(int(self.range_l), int(self.range_u) + 1)
        return amount in r
    
    def validate_part_two(self):
        i = int(self.range_l) - 1
        it = int(self.range_u) - 1
        p = self.password
        l = self.letter
        return (p[i] == l and p[it] != l) or (p[i] != l and p[it] == l)


def create_line(s):
    res = PATTERN.match(s)
    return Line(**res.groupdict())

lines = [create_line(s) for s in base_lines]

print('---- DAY TWO PART ONE ----')

result_one = [x for x in lines if x.validate()]

print(len(result_one))

print('---- DAY TWO PART TWO ----')

result_two = [x for x in lines if x.validate_part_two()]

print(len(result_two))

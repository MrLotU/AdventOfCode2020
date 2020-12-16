import re
import functools

TEST_INPUT = '''departure class: 0-1 or 4-19
row: 0-5 or 8-19
departure seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9'''


PATTERN = r'(?P<rules>(?:[a-z ]+: \d+-\d+ or \d+-\d+\n?)+)\n{2}your ticket:\n(?P<ticket>(?:\d+,?)+)\n+nearby tickets:\n(?P<other_tickets>(?:\d+,?\n?)+)'

with open('inputs/sixteen.txt', 'r') as f:
    input_text = f.read()
    # input_text = TEST_INPUT

parts = re.match(PATTERN, input_text).groupdict()

print('---- DAY SIXTEEN PART ONE ----') # 26941
def _range(a,b):
    return range(a, b+1)

def numarr_from_rule(r):
    ranges = r.split(': ')[-1]
    ranges = ranges.split(' or ')
    arr = []
    for _r in ranges:
        r = _range(*map(lambda e: int(e), _r.split('-')))
        arr.extend([i for i in r])
    return arr

tickets = parts['other_tickets'].split('\n')
rules = parts['rules'].split('\n')
valid_numbers = []
invalid_numbers = []
valid_tickets = []

for r in rules:
    valid_numbers.extend(numarr_from_rule(r))

for ticket in tickets:
    invalid_ticket_nums = [int(i) for i in ticket.split(',') if int(i) not in valid_numbers]
    if invalid_ticket_nums == []:
        valid_tickets.append(ticket)
    else:
        invalid_numbers.extend(invalid_ticket_nums)

print(functools.reduce(lambda a,b: a + b, invalid_numbers, 0))
print('---- DAY SIXTEEN PART TWO ----')

my_ticket = [int(x) for x in parts['ticket'].split(',')]
rules_dict = {}

for ticket in valid_tickets:
    for idx, value in enumerate([int(i) for i in ticket.split(',')]):
        v = rules_dict.get(idx, None)
        if not v:
            v = rules
        
        rules_dict[idx] = [r for r in v if value in numarr_from_rule(r)]

rules_list = sorted(rules_dict.items(), key=lambda e: len(e[-1]))

idx = 0
while True:
    index, rules = rules_list[idx]
    if len(rules) == 1:
        r = rules[0]
        for i in range(idx + 1, len(rules_list)):
            a,b = rules_list[i]
            _i = b.index(r)
            # print(idx, i, _i, (a, b[:_i] + b[_i+1:]))
            rules_list[i] = (a, b[:_i] + b[_i+1:])
        
    if idx == len(rules_list) - 1:
        break
    else:
        idx += 1

values = []
for (idx, rules) in rules_list:
    rule = rules[0]
    if rule.startswith('departure'):
        values.append(my_ticket[idx])

print(values)
print(functools.reduce(lambda a,b: a * b, values, 1))
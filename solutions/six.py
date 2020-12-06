import functools

TEST_INPUT = '''abc

a
b
c

ab
ac

a
a
a
a

b'''

with open(f'inputs/six.txt', 'r') as f:
    groups = f.read().split('\n\n')
    # groups = TEST_INPUT.split('\n\n')

print('---- DAY SIX PART ONE ----')

total_sum = 0

p_one = [len(set(x.replace('\n', ''))) for x in groups]
print(functools.reduce(lambda a, b: a + b, p_one))

print('---- DAY SIX PART TWO ----')

p_two_sum = 0

for group in groups:
    group_size = group.count('\n') + 1
    answers = group.replace('\n', '')
    s_answers = set(answers)
    for a in s_answers:
        if answers.count(a) == group_size:
            p_two_sum += 1

print(p_two_sum)
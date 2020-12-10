import functools

TEST_INPUT = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''

with open(f'inputs/ten.txt', 'r') as f:
    _numbers = [int(n) for n in f.read().split('\n')]
    # _numbers = [int(n) for n in TEST_INPUT.split('\n')]

print('---- DAY TEN PART ONE ----')

max_jolts = max(_numbers) + 3
numbers = sorted(_numbers + [0, max_jolts])

one_diffs = 0
three_diffs = 0
for idx, num in enumerate(numbers):
    if idx + 1 == len(numbers):
        continue
    r = numbers[idx + 1] - num
    if r == 1:
        one_diffs += 1
    elif r == 2:
        pass
    elif r == 3:
        three_diffs  += 1
    else:
        raise Exception(f'{idx}, {num}, {numbers[idx + 1]}, {r}')


print(one_diffs * three_diffs)

print('---- DAY TEN PART TWO ----')

num_map = {0: 1}
for num in numbers[1:]:
    prev_three = [num_map.get(num - i, 0) for i in range(1, 4)]
    num_map[num] = functools.reduce(lambda a, b: a + b, prev_three)

print(num_map[max_jolts])
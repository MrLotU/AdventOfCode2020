TEST_INPUT = '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''

with open(f'inputs/nine.txt', 'r') as f:
    numbers = [int(n) for n in f.read().split('\n')]
    # numbers = [int(n) for n in TEST_INPUT.split('\n')]

print('---- DAY NINE PART ONE ----')

STEP_SIZE = 25 if len(numbers) > 20 else 5

FAULTY_NUMBER = 0

for idx, n in enumerate(numbers[STEP_SIZE:]):
    r = numbers[idx:idx+STEP_SIZE]
    f = False
    for num in r:
        if n - num in r and n != num:
            f = True
    if f:
        continue
    FAULTY_NUMBER = n

print(FAULTY_NUMBER)

print('---- DAY NINE PART TWO ----')

for idx, n in enumerate(numbers):
    if n >= FAULTY_NUMBER:
        continue
    
    f = False
    for i in range(idx, len(numbers)):
        sub = numbers[idx:i]
        s = sum(sub)
        if s == FAULTY_NUMBER:
            f = True
            print('Found the range!', sub, 'solution:', min(sub) + max(sub))
        if s >=  FAULTY_NUMBER:
            break
    if f:
        break
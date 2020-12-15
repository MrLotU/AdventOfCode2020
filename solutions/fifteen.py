TEST_INPUT = '0,3,6'

with open('inputs/fifteen.txt', 'r') as f:
    numbers = f.read().split(',')
    # numbers = TEST_INPUT.split(',')

def find_number_at(turn):
    num_map = {}
    sequence = ['x'] + [int(i) for i in numbers]

    def set_num_or_default(num, idx):
        if num not in num_map:
            num_map[num] = idx
        else:
            _i = num_map[num]
            if isinstance(_i, tuple):
                _i = _i[-1]
            num_map[num] = (_i, idx)

    for idx, n in enumerate(sequence):
        set_num_or_default(n, idx)

    for i in range(len(sequence), turn + 1):
        lv = sequence[i - 1]
        if num_map[lv] == i - 1:
            sequence.append(0)
            set_num_or_default(0, i)
        else:
            before, last = num_map[lv]
            sequence.append(last - before)
            set_num_or_default(last - before, i)
        
        # print(sequence, num_map)

    return sequence[-1]
print('---- DAY FIFTEEN PART ONE ----')
print(find_number_at(2020))
print('---- DAY FIFTEEN PART TWO ----')
print(find_number_at(30000000))
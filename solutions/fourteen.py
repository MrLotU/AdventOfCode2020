import functools

TEST_INPUT = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''

with open('inputs/fourteen.txt', 'r') as f:
    lines = f.read().split('\n')
    # lines = TEST_INPUT.split('\n')


def binlist(ml, x):
    return list(reversed([str((x >> i) & 1) for i in range(ml)]))


print('---- DAY FOURTEEN PART ONE ----')

mem_map = {}
mask = ''


def apply_mask(number):
    masklen = len(mask)
    binstring = binlist(masklen, number)
    for i, v in enumerate(mask):
        if v != 'X':
            binstring[i] = v
    return int(''.join(binstring), 2)


for l in lines:
    if l[:2] == 'ma':
        mask = l.split(' = ')[-1]

    else:
        num = int(l.split(' = ')[-1])
        idx = int(l.split('[')[-1].split(']')[0])
        n = apply_mask(num)
        mem_map[idx] = n
        # print(f'Line {l} masked to {n} at index {idx}\n')

print(functools.reduce(lambda a, b: a + b, list(mem_map.values())))

print('---- DAY FOURTEEN PART TWO ----')

mem_map = {}
mask = ''

def mask_address(number):
    masklen = len(mask)
    binary = binlist(masklen, number)
    print(f'{"".join(binary)}\n{mask}')
    for i, v in enumerate(mask):
        if v != '0':
            binary[i] = v
    indices = [i for i, x in enumerate(binary) if x == 'X']
    print("".join(binary))
    x_count = len(indices)
    print(x_count, x_count ** 2)
    for i in range(x_count ** 2):
        temp_mask = binlist(x_count, i)
        print(''.join(temp_mask))
        j = 0
        # b = binary[:]
        for idx in indices:
            # print(idx)
            binary[idx] = temp_mask[j]
            j += 1
        
        print(f'{"".join(binary)}, {int("".join(binary), 2)}')
        yield int(''.join(binary), 2)
    print('\n')

for l in lines:
    if l[:2] == 'ma':
        mask = l.split(' = ')[-1]
    
    else:
        num = int(l.split(' = ')[-1])
        idx = int(l.split('[')[-1].split(']')[0])
        
        posBin = binlist(len(mask), idx)
        mask = mask
        maskIds = []

        for i, v in enumerate(mask):
            if v == 'X':
                maskIds.append(i)
            if v == '0':
                continue
            posBin[i] = v
        
        for i in range(len(posBin) ** 2):
            temp_mask = binlist(len(maskIds), i)
            j = 0
            for id in maskIds:
                posBin[id] = temp_mask[j]
                j += 1
            mem_map[int(''.join(posBin), 2)] = num

        # for ad in mask_address(idx):
        #     # print(f'Line {l} masked to {num} at index {ad}\n')
        #     mem_map[ad] = num

print(functools.reduce(lambda a, b: a + b, list(mem_map.values())))

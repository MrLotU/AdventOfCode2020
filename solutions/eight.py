TEST_INPUT = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''


with open(f'inputs/eight.txt', 'r') as f:
    _lines = f.read().split('\n')
    # _lines = TEST_INPUT.split('\n')

print('---- DAY EIGHT PART ONE ----')

used_map = {}
storage = {}

def map_hash(lines, index=''):
    return ';;'.join(lines) + str(index)

def handle_line(index, lines):
    a = storage.get(map_hash(lines), 0)
    if used_map.get(map_hash(lines, index), False):
        return (1, a)
    if index >= len(lines):
        return (0, a)
    line = lines[index]
    used_map[map_hash(lines, index)] = True
    cmd, num = line.split(' ')
    num = int(num)
    if cmd == 'acc':
        storage[map_hash(lines)] = a + num
        return handle_line(index + 1, lines)
    elif cmd == 'jmp':
        return handle_line(index + num, lines)
    elif cmd == 'nop':
        return handle_line(index + 1, lines)
    else:
        return (1, 0)

print(handle_line(0, _lines))

print('---- DAY EIGHT PART TWO ----')

used_map = {}
storage = {}

def recurse_line(index, lines):
    a = storage.get(map_hash(lines), 0)
    if used_map.get(map_hash(lines, index), False):
        return (1, a)
    if index >= len(lines):
        return (0, a)
    line = lines[index]
    used_map[map_hash(lines, index)] = True
    cmd, n = line.split(' ')
    num = int(n)
    if cmd == 'acc':
        storage[map_hash(lines)] = a + num
        return recurse_line(index + 1, lines)
    elif cmd == 'jmp':
        lines_copy = lines.copy()
        lines_copy[index] = f'nop {n}'
        a, b = handle_line(0, lines_copy)
        if a == 0:
            print(f'Fixed program by changing line {index} from {line} to nop {n}')
            return (a, b)
        return recurse_line(index + num, lines)
    elif cmd == 'nop':
        lines_copy = lines.copy()
        lines_copy[index] = f'jmp {n}'
        a, b = handle_line(0, lines_copy)
        if a == 0:
            print(f'Fixed program by changing line {index} from {line} to jmp {n}')
            return (a, b)
        return recurse_line(index + 1, lines)
    else:
        raise Exception("Invalid command")

print(recurse_line(0, _lines))
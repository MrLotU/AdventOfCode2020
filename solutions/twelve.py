TEST_INPUT = '''F10
N3
F7
R90
F11'''

with open('inputs/twelve.txt', 'r') as f:
    instructions = f.read().split('\n')
    # instructions = TEST_INPUT.split('\n')

print('---- DAY TWELVE PART ONE ----')

operation_map = {
    'N': lambda ns, ew, f, i: (ns + i, ew, f),
    'S': lambda ns, ew, f, i: (ns - i, ew, f),
    'E': lambda ns, ew, f, i: (ns, ew + i, f),
    'W': lambda ns, ew, f, i: (ns, ew - i, f),
    'P': lambda ns, ew, f, i: (ns, ew, i),
}

POSITIONS = ['N', 'E', 'S', 'W']


def update_position_from_input(instruction, position):
    op = instruction[0]
    num = int(instruction[1:])

    if op in POSITIONS:
        position = operation_map[op](*position, num)
    elif op in ['L', 'R']:
        turns = int(num / 90) * (-1 if op == 'L' else 1)
        idx = POSITIONS.index(position[2]) + turns
        while idx >= len(POSITIONS):
            idx -= len(POSITIONS)

        new_pos = POSITIONS[idx]
        position = operation_map['P'](*position, new_pos)
    else:
        position = operation_map[position[2]](*position, num)

    return position


pos = (0, 0, 'E')

for ins in instructions:
    pos = update_position_from_input(ins, pos)

ns, ew, f = pos
print(abs(ns) + abs(ew))

print('---- DAY TWELVE PART TWO ----')

waypoint_map = {
    'N': lambda ns, ew, i: (ns + i, ew),
    'S': lambda ns, ew, i: (ns - i, ew),
    'E': lambda ns, ew, i: (ns, ew + i),
    'W': lambda ns, ew, i: (ns, ew - i),
    'F': lambda ns, ew, wns, wew, i: ((wns * i) + ns, (wew * i) + ew)
}

rotation_map = {
    'NE': lambda ns, ew: (ew * -1, ns),
    'NS': lambda ns, ew: (ns * -1, ew * -1),
    'NW': lambda ns, ew: (ew, ns * -1),

    'EN': lambda ns, ew: (ew, ns * -1),
    'ES': lambda ns, ew: (ew * -1, ns),
    'EW': lambda ns, ew: (ns * -1, ew * -1),

    'SN': lambda ns, ew: (ns * -1, ew * -1),
    'SE': lambda ns, ew: (ew, ns * -1),
    'SW': lambda ns, ew: (ew * -1, ns),

    'WN': lambda ns, ew: (ew * -1, ns),
    'WE': lambda ns, ew: (ns * -1, ew * -1),
    'WS': lambda ns, ew: (ew, ns * -1)
}

ship_pos = (0, 0, 'N', 1, 10)


def update_waypoint_and_ship(instruction, position):
    op = instruction[0]
    num = int(instruction[1:])

    if op in POSITIONS:
        ns, ew = waypoint_map[op](*position[3:], num)
        position = (*position[:3], ns, ew)
    elif op in ['L', 'R']:
        turns = int(num / 90) * (-1 if op == 'L' else 1)
        facing = position[2]
        ns, ew = position[3:]
        ans, aew = abs(ns), abs(ew)
        idx = POSITIONS.index(facing) + turns
        while idx >= len(POSITIONS):
            idx -= len(POSITIONS)

        new_pos = rotation_map[facing + POSITIONS[idx]](ns, ew)

        position = (*position[:2], POSITIONS[idx], *new_pos)
    else:
        ns, ew, f, wns, wew = position
        ns, ew = waypoint_map[op](*position[:2], *position[3:], num)
        position = (ns, ew, f, wns, wew)

    return position


for ins in instructions:
    ship_pos = update_waypoint_and_ship(ins, ship_pos)

ns, ew, f, wns, wew = ship_pos
print(abs(ns) + abs(ew))

TEST_INPUT = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''


def get_input():
    with open(f'inputs/eleven.txt', 'r') as f:
        rows = [[t for t in x] for x in f.read().split('\n')]
        # rows = [[t for t in x] for x in TEST_INPUT.split('\n')]

    return rows


print('---- DAY ELEVEN PART ONE ----')

rows = get_input()
width = len(rows[0])
height = len(rows)


def adjacent_coords(coord):
    x, y = coord
    adjacents = []

    if x - 1 >= 0:
        adjacents.append((x - 1, y))
        if y - 1 >= 0:
            adjacents.append((x - 1, y - 1))
        if y + 1 < height:
            adjacents.append((x - 1, y + 1))

    if x + 1 < width:
        adjacents.append((x + 1, y))
        if y - 1 >= 0:
            adjacents.append((x + 1, y - 1))
        if y + 1 < height:
            adjacents.append((x + 1, y + 1))

    if y - 1 >= 0:
        adjacents.append((x, y - 1))

    if y + 1 < height:
        adjacents.append((x, y + 1))

    return adjacents


def row_for(coord):
    x, y = coord
    return rows[y][x]


def update_seat_for(coord, status):
    x, y = coord
    shadow_rows[y][x] = status
    return shadow_rows


def modify_based_on_adjacents(coord, current, adjacents, limit):
    mods = 0
    if current == 'L' and adjacents.count('#') == 0:
        mods += 1
        update_seat_for(coord, '#')
    elif current == '#' and adjacents.count('#') >= limit:
        mods += 1
        update_seat_for(coord, 'L')

    return mods


while True:
    shadow_rows = [x[:] for x in rows]
    mods = 0

    for y in range(height):
        for x in range(width):
            coord = (x, y)
            current = row_for(coord)
            if current == '.':
                continue
            adjacents = [row_for(x) for x in adjacent_coords(coord)]
            mods += modify_based_on_adjacents(coord, current, adjacents, 4)

    if mods == 0:
        break
    else:
        rows = [x[:] for x in shadow_rows]

big_string = '\n'.join([''.join(t) for t in rows])
print(big_string.count('#'))

print('---- DAY ELEVEN PART TWO ----')


def semi_adjacent_statuses(coord):
    adjacents = []
    x, y = coord

    for i in range(x - 1, -1, -1):
        r = row_for((i, y))
        if r in ['L', '#']:
            adjacents.append(r)
            break

    for i in range(x + 1, width):
        r = row_for((i, y))
        if r in ['L', '#']:
            adjacents.append(r)
            break

    for i in range(y - 1, -1, -1):
        r = row_for((x, i))
        if r in ['L', '#']:
            adjacents.append(r)
            break

    for i in range(y + 1, height):
        r = row_for((x, i))
        if r in ['L', '#']:
            adjacents.append(r)
            break

    for ix, iy in zip(range(x - 1, -1, -1), range(y - 1, -1, -1)):
        r = row_for((ix, iy))
        if r in ['L', '#']:
            adjacents.append(r)
            break

    for ix, iy in zip(range(x + 1, width), range(y - 1, -1, -1)):
        r = row_for((ix, iy))
        if r in ['L', '#']:
            adjacents.append(r)
            break

    for ix, iy in zip(range(x - 1, -1, -1), range(y + 1, height)):
        r = row_for((ix, iy))
        if r in ['L', '#']:
            adjacents.append(r)
            break

    for ix, iy in zip(range(x + 1, width), range(y + 1, height)):
        r = row_for((ix, iy))
        if r in ['L', '#']:
            adjacents.append(r)
            break

    if len(adjacents) > 8:
        raise Exception('Bweebwoo')
    return adjacents


rows = get_input()
width = len(rows[0])
height = len(rows)

while True:
    shadow_rows = [x[:] for x in rows]
    mods = 0

    for y in range(height):
        for x in range(width):
            coord = (x, y)
            current = row_for(coord)
            if current == '.':
                continue
            adjacents = semi_adjacent_statuses(coord)
            mods += modify_based_on_adjacents(coord, current, adjacents, 5)

    if mods == 0:
        break
    else:
        rows = [x[:] for x in shadow_rows]

big_string = '\n'.join([''.join(t) for t in rows])
print(big_string.count('#'))

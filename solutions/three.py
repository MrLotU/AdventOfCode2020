TEST_INPUT = '''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''

with open(f'inputs/three.txt', 'r') as f:
    base_lines = f.read().split('\n')
    # base_lines = TEST_INPUT.split('\n')

MAX_Y_COORDINATE = len(base_lines)
COORD_RANGE = range(0, MAX_Y_COORDINATE)

def count_trees(coordinates):
    t = 0
    for idx, coord in enumerate(coordinates):
        if coord[1] >= MAX_Y_COORDINATE:
            return t
        line = base_lines[coord[1]]
        while coord[0] >= len(line):
            line = line + line
        
        char = line[coord[0]]
        if char == '#':
            t += 1
    return t

print('---- DAY THREE PART ONE ----')

print(count_trees([(t * 3, t)   for t in COORD_RANGE]))

print('---- DAY THREE PART TWO ----')

rodo = count_trees([(t, t)      for t in COORD_RANGE])
rtdo = count_trees([(t * 3, t)  for t in COORD_RANGE])
rfdo = count_trees([(t * 5, t)  for t in COORD_RANGE])
rsdo = count_trees([(t * 7, t)  for t in COORD_RANGE])
rodt = count_trees([(t, t * 2)  for t in COORD_RANGE])

print(rodo * rtdo * rfdo * rsdo * rodt)
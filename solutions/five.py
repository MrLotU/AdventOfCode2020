TEST_INPUT = '''BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL'''

with open(f'inputs/five.txt', 'r') as f:
    passes = f.read().split('\n')
    # passes = TEST_INPUT.split('\n')

print('---- DAY FIVE PART ONE ----')

def split_calc(letters, r):
    if len(r) == 1:
        return r[0]
    l = letters[0]
    split_idx = int(len(r) / 2)
    if l in ['F', 'L']:
        return split_calc(letters[1:], r=r[:split_idx])
    elif l in ['B', 'R']:
        return split_calc(letters[1:], r=r[split_idx:])

seat_ids = []

for p in passes:
    seat = (split_calc(p[:7], range(0, 128)) * 8) + split_calc(p[7:], range(0, 8))
    seat_ids.append(seat)

print(max(seat_ids))

print('---- DAY FIVE PART TWO ----')

seats = len(seat_ids)
seat_ids = sorted(seat_ids)
for idx, seat in enumerate(seat_ids):
    if idx + 1 == seats:
        break
    if seat_ids[idx + 1] != seat + 1:
        print(seat + 1)

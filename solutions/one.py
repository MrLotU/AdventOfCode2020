with open('inputs/one.txt', 'r') as f:
    s = f.read().split('\n')
    _lines = {int(x): int(x) for x in s}
    lines = list(_lines.keys())

print('---- DAY ONE PART ONE ----')

for num in lines:
    n = 2020 - num
    if _lines.get(n) is not None:
        print(n * num)
        break

# for i, num in enumerate(lines):
#     for n in lines[i:]:
#         if num + n == 2020 and num != n:
#             print(num * n)

print('---- DAY ONE PART TWO ----')

for i, num in enumerate(lines):
    for n in lines[i:]:
        nn = 2020 - num - n
        if _lines.get(nn) is not None:
            print(n * num * nn)
            break
    else:
        continue
    break


# for i, num in enumerate(lines):
#     for ii, n in enumerate(lines[i:]):
#         for nn in lines[ii:]:
#             if num + n + nn == 2020 and num != n and num != nn and n != nn:
#                 print(num * n * nn)

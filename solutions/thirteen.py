with open('inputs/thirteen.txt', 'r') as f:
    timestamp = int(f.readline())
    # timestamp = 939
    buslines = f.readline().split(',')
    # buslines = '7,13,x,x,59,x,31,19'.split(',')

print('---- DAY THIRTEEN PART ONE ----')

actual_buslines = list(filter(lambda e: e != 'x', buslines))
now = timestamp
while True:
    now += 1
    line = next((x for x in actual_buslines if now % int(x) == 0), None)
    if line:
        print((now - timestamp) * int(line))
        break

print('---- DAY THIRTEEN PART TWO ----')

bus = [int(x) for x in actual_buslines]
a = [-i for i, x in enumerate(buslines) if x != 'x']


def crt(a, b):
    if a-b == 1:
        return 1, -1
    q, r = a // b, a % b
    m, n = crt(b, r)
    return n, m-n*q


prod = 1
for b in bus:
    prod *= b

ans = 0

for i, b in enumerate(bus):
    m, n = crt(prod // b, b)
    ans += a[i] % b * m * prod // b

print(ans % prod)

import re

TEST_INPUT = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''

with open(f'inputs/four.txt', 'r') as f:
    passports = f.read().split('\n\n')
    # passports = TEST_INPUT.split('\n\n')

PATTERN = re.compile(r'(ecl|pid|eyr|hcl|byr|iyr|hgt):', re.MULTILINE)

print('---- DAY FOUR PART ONE ----')

VALIDS = 0
REQUIREDS = sorted(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

part_one_passports = [p for p in passports if sorted(
    PATTERN.findall(p)) == REQUIREDS]

print(len(part_one_passports))

print('---- DAY FOUR PART TWO ----')

PATTERN_PART_TWO = re.compile(
    r'(ecl|pid|eyr|hcl|byr|iyr|hgt):([\w\d#]+)', re.MULTILINE)


def between(a, b, c):
    return a >= b and a <= c


LAMBDA_MAP = {
    'byr': lambda e: between(int(e), 1920, 2002),
    'iyr': lambda e: between(int(e), 2010, 2020),
    'eyr': lambda e: between(int(e), 2020, 2030),
    'hgt': lambda e: e[-2:] in ['in', 'cm'] and between(int(e[:-2]), 150 if e[-2:] == 'cm' else 59, 193 if e[-2:] == 'cm' else 76),
    'hcl': lambda e: re.match(r'^#[0-9a-f]{6}$', e) is not None,
    'ecl': lambda e: e in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda e: re.match(r'^[0-9]{9}$', e) is not None
}

VALIDS_TWO = 0
for p in part_one_passports:
    tuples = PATTERN_PART_TWO.findall(p)
    try:
        for (k, v) in tuples:
            if not LAMBDA_MAP[k](v):
                raise Exception()
        VALIDS_TWO += 1
    except:
        continue

print(VALIDS_TWO)

import sys


input = open(sys.argv[1], 'r').read().strip()
banks = [[int(x) for x in line] for line in input.split('\n')]


def first_max(l):
    m = l[0]
    i = 0
    for j in range(1, len(l)):
        if l[j] > m:
            m = l[j]
            i = j
    return m, i

def turn_on_two(bank):
    fm, fi = first_max(bank[:-1])
    sm, si = first_max(bank[fi+1:])
    return fm, sm

def bank_joltage(bank):
    s = 0
    for b in bank:
        s = s*10+b
    return s

def total_joltage(banks):
    return sum(bank_joltage(bank) for bank in banks)

turned_on = [turn_on_two(bank) for bank in banks]
print(total_joltage(turned_on))


def turn_on_n(bank, n):
    if n == 1:
        return [max(bank)]
    m, i = first_max(bank[:-(n-1)])
    return [m] + turn_on_n(bank[i+1:], n-1)

turned_on = [turn_on_n(bank, 12) for bank in banks]
print(total_joltage(turned_on))


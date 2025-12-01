import sys


input = open(sys.argv[1], 'r').read().strip()
rotations = [(l[0], int(l[1:])) for l in input.split('\n')]


def count_zeros(rotations):
    dial = 50
    count = 0
    for d, n in rotations:
        dial = (dial + (1 if d == 'R' else -1) * n) % 100
        if dial == 0:
            count += 1
    return count

print(count_zeros(rotations))


def count_zeros_every_tick(rotations):
    dial = 50
    count = 0
    for d, n in rotations:
        direc = 1 if d == 'R' else -1
        for _ in range(n):
            dial = (dial + direc) % 100
            if dial == 0:
                count += 1
    return count

print(count_zeros_every_tick(rotations))


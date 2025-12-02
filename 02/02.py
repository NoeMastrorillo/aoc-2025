import sys
import math
import functools


input = open(sys.argv[1], 'r').read().strip()
ranges = [(int(s), int(e)) for s,e in map(lambda x: x.split('-'), input.split(','))]


def is_repetitive(i):
    n = math.ceil(math.log(i+1, 10))
    if n % 2:
        return False
    x = 10**(n//2)
    return i//x == i%x

def find_repetitive_ids(ranges):
    invalid = []
    for s, e in ranges:
        for i in range(s, e+1):
            if is_repetitive(i):
                invalid.append(i)
    return invalid

print(sum(find_repetitive_ids(ranges)))


@functools.cache
def divisors(n):
    div = []
    for i in range(1, n):
        if n%i == 0:
            div.append(i)
    return div

def has_pattern_of_size(i, n, d):
    pattern = None
    x = 10**d
    y = 1
    for j in range(n//d):
        part = i//y%x
        y *= x
        if pattern is None:
            pattern = part
        elif part != pattern:
            return False
    return True

def has_repeating_pattern(i):
    n = math.ceil(math.log(i+1, 10))
    for d in divisors(n):
        if has_pattern_of_size(i, n, d):
            return True
    return False

def find_invalid_ids(ranges):
    invalid = []
    for s, e in ranges:
        for i in range(s, e+1):
            if has_repeating_pattern(i):
                invalid.append(i)
    return invalid

print(sum(find_invalid_ids(ranges)))


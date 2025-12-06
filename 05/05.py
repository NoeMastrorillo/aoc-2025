import sys


input = open(sys.argv[1], 'r').read().strip()
input_ranges, input_ids = input.split('\n\n')
ranges = [(int(s), int(e)) for s,e in [line.split('-') for line in input_ranges.split('\n')]]
ids = [int(id) for id in input_ids.split('\n')]


def is_in_range(i, r):
    s, e = r
    return s <= i <= e

def is_fresh(i, ranges):
    for r in ranges:
        if is_in_range(i, r):
            return True
    return False

print(sum(is_fresh(i, ranges) for i in ids))


def fresh_ids(r):
    s, e = r
    return set(range(s, e+1))

def all_fresh_ids(ranges):
    return set().union(*(fresh_ids(r) for r in ranges))

def position(x, complex_range):
    for i, (si, ei) in enumerate(complex_range):
        if x < si:
            return i-1, i 
        if is_in_range(x, (si, ei)):
            return i
    return len(ranges)-1, len(ranges)


def merge(simple_range, complex_range):
    s, e = simple_range
    ps = position(s, complex_range)
    pe = position(e, complex_range)

    if ps == pe:
        if type(ps) is int:
            # subset of a range
            return complex_range
        else:
            # range between two ranges
            _, i = ps
            return complex_range[:i] + [simple_range] + complex_range[i:]

    if type(ps) is int and type(pe) is int:
        sn, _ = complex_range[ps]
        _, en = complex_range[pe]
        return complex_range[:ps] + [(sn, en)] + complex_range[pe+1:]

    if type(ps) is int:
        _, j = pe
        sn, _ = complex_range[ps]
        return complex_range[:ps] + [(sn, e)] + complex_range[j:]

    if type(pe) is int:
        _, i = ps
        _, en = complex_range[pe]
        return complex_range[:i] + [(s, en)] + complex_range[pe+1:]

    _, i = ps
    _, j = pe
    return complex_range[:i] + [(s,e)] + complex_range[j:]

def merge_all(ranges):
    complex_range = []
    for r in ranges:
        complex_range = merge(r, complex_range)
    return complex_range

def length(complex_range):
    return sum(e-s+1 for s,e in complex_range)

print(length(merge_all(ranges)))


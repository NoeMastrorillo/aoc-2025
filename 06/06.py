import sys
import numpy as np
import functools as ft


input = open(sys.argv[1], 'r').read().strip()


def apply(numbers, operations):
    mask_add = operations == '+'
    mask_mult = operations == '*'
    result = np.zeros(numbers.shape[0])
    result[mask_add] = np.add.reduce(numbers[mask_add], axis=1)
    result[mask_mult] = np.multiply.reduce(numbers[mask_mult], axis=1)
    return result

lines = [list(line.split()) for line in input.split('\n')]
numbers1 = np.transpose([[int(x) for x in line] for line in lines[:-1]])
operations1 = np.array(lines[-1])
print(np.sum(apply(numbers1, operations1)))


def split_array(arr, v):
    result = []
    line = []
    for x in arr:
        if x == v:
            result.append(line)
            line = []
        else:
            line.append(x)
    result.append(line)
    return result

def reduce(ns, op):
    if op == '+':
        return ft.reduce(lambda acc, x: acc+x, ns)
    return ft.reduce(lambda acc, x: acc*x, ns, 1)

chars = np.transpose([list(line) for line in input.split('\n')[:-1]])
groups = [int(ft.reduce(lambda acc, c: acc + c if c != ' ' else acc, line, '0')) for line in chars]
numbers2 = split_array(groups, 0)[::-1]
operations2 = operations1[::-1]
print(sum(map(lambda x: reduce(*x), zip(numbers2, operations2))))


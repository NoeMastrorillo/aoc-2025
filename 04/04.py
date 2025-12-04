import sys
import numpy as np


input = open(sys.argv[1], 'r').read().strip()
grid = np.array([list(line) for line in input.split('\n')]) == '@'


def count_surrounding(grid, i, j):
    r, c = grid.shape
    count = 0
    for di in range(-1, 2):
        if 0 <= i+di < r:
            for dj in range(-1, 2):
                if 0 <= j+dj < r and (di != 0 or dj != 0):
                    count += grid[i+di,j+dj]
    return count

def accessible_rolls(grid):
    r, c = grid.shape
    out = np.zeros((r, c), dtype=bool)
    for i in range(r):
        for j in range(c):
            if grid[i,j]:
                out[i,j] = (count_surrounding(grid, i, j) < 4)
    return out 

print(np.sum(accessible_rolls(grid)))


def repeat_remove(grid):
    accessible = accessible_rolls(grid)
    nremove = np.sum(accessible)
    count = 0
    while (nremove := np.sum(accessible_rolls(grid))) > 0:
        count += nremove
        grid = grid ^ accessible
        accessible = accessible_rolls(grid)
        nremove = np.sum(accessible)
    return count

print(repeat_remove(grid))


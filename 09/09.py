import sys
import numpy as np


input = open(sys.argv[1], 'r').read().strip()
tiles = np.array([line.split(',') for line in input.split('\n')], dtype=int)


def max_area(tiles):
    n = tiles.shape[0]
    area = 0
    for i in range(n):
        x1, y1 = tiles[i]
        for j in range(i+1, n):
            x2, y2 = tiles[j]
            a = (abs(x1-x2)+1)*(abs(y1-y2)+1)
            if a > area:
                area = a
    return area

print(max_area(tiles))


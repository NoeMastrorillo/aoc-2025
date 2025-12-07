import sys
from collections import defaultdict


input = open(sys.argv[1], 'r').read().strip()
grid = [list(l) for l in input.split('\n')]
nrows = len(grid)
ncols = len(grid[0])
start_pos = (0, grid[0].index('S'))

splitters = set()
for i in range(nrows):
    for j in range(ncols):
        if grid[i][j] == '^':
            splitters.add((i,j))


def count_splits(nrows, ncols, splitters, start_pos):
    beams = {start_pos}
    splits = 0
    for _ in range(1, nrows):
        new_beams = set()
        for i,j in beams:
            if (i+1, j) in splitters:
                new_beams.add((i+1, j-1))
                new_beams.add((i+1, j+1))
                splits += 1
            else:
                new_beams.add((i+1, j))
        beams = new_beams
    return splits

print(count_splits(nrows, ncols, splitters, start_pos))


def count_timelines(nrows, ncols, splitters, start_pos):
    beams = defaultdict(int)
    beams[start_pos] = 1
    for _ in range(1, nrows):
        new_beams = defaultdict(int)
        for (i,j), tl in beams.items():
            if (i+1, j) in splitters:
                new_beams[(i+1,j-1)] += tl
                new_beams[(i+1,j+1)] += tl
            else:
                new_beams[(i+1,j)] += tl
            beams = new_beams
    return sum(tl for (i,j),tl in beams.items() if i == nrows-1)

print(count_timelines(nrows, ncols, splitters, start_pos))


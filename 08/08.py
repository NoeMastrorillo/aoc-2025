import sys
import numpy as np
import itertools


input = open(sys.argv[1], 'r').read().strip()
lines = [l.split(',') for l in input.split('\n')]
boxes = np.array(lines, dtype=int)
nboxes = boxes.shape[0]

def distances(boxes):
    n = boxes.shape[0]
    return {(i,j): np.linalg.norm(boxes[i]-boxes[j]) for i,j in itertools.product(range(n), range(n)) if i > j}

def update_circuits(circuits, i, j):
    ci, cj = circuits[i], circuits[j]
    match (ci, cj):
        case (0, 0):
            circuits[[i,j]] = np.max(circuits)+1
        case (0, c):
            circuits[i] = circuits[j]
        case (c, 0):
            circuits[j] = circuits[i]
        case (a, b):
            circuits[circuits == b] = a

def connect_n(dists, nboxes, steps):
    sorted_dists = sorted(dists.items(), key=lambda kv: kv[1])
    circuits = np.zeros(nboxes)
    for k in range(steps):
        (i,j), d = sorted_dists[k]
        update_circuits(circuits, i, j)
    return circuits

def max_circuit_counts(circuits, n):
    _, counts = np.unique(circuits[circuits != 0], return_counts=True)
    return np.sort(counts)[-n:]

dists = distances(boxes)
circuits = connect_n(dists, nboxes, int(sys.argv[2]))
c1, c2, c3 = max_circuit_counts(circuits, 3)
print(c1*c2*c3)


def connect_all(dists, nboxes):
    sorted_dists = iter(sorted(dists.items(), key=lambda kv: kv[1]))
    circuits = np.zeros(nboxes)
    while np.any(circuits == 0) or np.unique(circuits).shape[0] > 1:
        (i,j), d = next(sorted_dists)
        update_circuits(circuits, i, j)
    return i, j

i, j = connect_all(dists, nboxes)
print(boxes[i,0]*boxes[j,0])


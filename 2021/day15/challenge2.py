from itertools import product
from pathlib import Path
from queue import PriorityQueue
import numpy as np

input_file = Path(__file__).parent / "in.txt"

matrix = []
with input_file.open("r") as f:
    for line in f.readlines():
        matrix.append([int(i) for i in line if i != "\n"])

matrix = np.asarray(matrix, dtype=float)
matrix = np.concatenate([matrix + i for i in range(0, 5)], axis=0)
matrix = np.concatenate([matrix + i for i in range(0, 5)], axis=1)

matrix[matrix > 9] = matrix[matrix > 9] - 9

costs = np.full_like(matrix, np.inf, dtype=float)

start = (0, 0)
end = (matrix.shape[0] - 1, matrix.shape[1] - 1)

costs[start] = 0

q = PriorityQueue()
q.put((0, start))

while costs[end] == np.inf:
    cost, (x, y) = q.get()
    for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if i < 0 or j < 0 or i >= matrix.shape[0] or j >= matrix.shape[1]:
            continue
        if costs[i, j] != np.inf:
            continue
        costs[i, j] = costs[x, y] + matrix[i, j]
        q.put((costs[i, j], (i, j)))

print(costs[end])

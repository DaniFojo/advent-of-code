import itertools
from pathlib import Path

import numpy as np

input_file = Path(__file__).parent / "in.txt"

matrix = []
with input_file.open("r") as f:
    for line in f.readlines():
        matrix.append([int(i) for i in line if i != "\n"])

matrix = np.asarray(matrix)
steps = 100
flashes = 0

for _ in range(steps):
    matrix += 1
    new_flashes_ths_step = set((i, j) for i, j in zip(*np.where(matrix == 10)))
    total_flashes_this_step = new_flashes_ths_step.copy()
    while new_flashes_ths_step:
        for i, j in new_flashes_ths_step.copy():
            new_flashes_ths_step.discard((i, j))
            for new_i, new_j in itertools.product([i - 1, i, i + 1], [j - 1, j, j + 1]):
                if not (
                    (new_i < 0)
                    or (new_i >= matrix.shape[0])
                    or (new_j < 0)
                    or (new_j >= matrix.shape[1])
                    or ((new_i, new_j) in total_flashes_this_step)
                ):
                    matrix[new_i, new_j] += 1
                    if matrix[new_i, new_j] == 10:
                        new_flashes_ths_step.add((new_i, new_j))
                        total_flashes_this_step.add((new_i, new_j))

    flashes += len(total_flashes_this_step)
    matrix[matrix > 9] = 0
print(flashes)

from pathlib import Path

import numpy as np

input_file = Path(__file__).parent / "in.txt"

matrix = []
with input_file.open("r") as f:
    for line in f.readlines():
        matrix.append([int(c) for c in line if c != "\n"])

matrix = np.asarray(matrix)


def basin_size(i, j, used_points):
    used_points.add((i, j))
    if (
        i < 0
        or i >= matrix.shape[0]
        or j < 0
        or j >= matrix.shape[1]
        or matrix[i, j] == 9
    ):
        return 0
    return (
        1
        + (basin_size(i - 1, j, used_points) if (i - 1, j) not in used_points else 0)
        + (basin_size(i + 1, j, used_points) if (i + 1, j) not in used_points else 0)
        + (basin_size(i, j - 1, used_points) if (i, j - 1) not in used_points else 0)
        + (basin_size(i, j + 1, used_points) if (i, j + 1) not in used_points else 0)
    )


sizes = []
used_points = set()
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if matrix[i, j] == 9:
            used_points.add((i, j))
            continue
        if (i, j) in used_points:
            continue
        sizes.append(basin_size(i, j, used_points))


sizes = sorted(sizes)
print(sizes[-1] * sizes[-2] * sizes[-3])

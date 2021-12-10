from pathlib import Path

import numpy as np

input_file = Path(__file__).parent / "in.txt"

matrix = []
with input_file.open("r") as f:
    for line in f.readlines():
        matrix.append([int(c) for c in line if c != "\n"])

matrix = np.asarray(matrix)


def is_low(i, j):
    p = matrix[i, j]
    if i == j == 0:
        return matrix[i + 1, j] > p and matrix[i, j + 1] > p
    elif i == matrix.shape[0] - 1 and j == matrix.shape[1] - 1:
        return matrix[i - 1, j] > p and matrix[i, j - 1] > p
    elif i == 0 and j == matrix.shape[1] - 1:
        return matrix[i + 1, j] > p and matrix[i, j - 1] > p
    elif i == matrix.shape[0] - 1 and j == 0:
        return matrix[i - 1, j] > p and matrix[i, j + 1] > p
    elif i == 0:
        return matrix[i + 1, j] > p and matrix[i, j - 1] > p and matrix[i, j + 1] > p
    elif i == matrix.shape[0] - 1:
        return matrix[i - 1, j] > p and matrix[i, j - 1] > p and matrix[i, j + 1] > p
    elif j == 0:
        return matrix[i + 1, j] > p and matrix[i - 1, j] > p and matrix[i, j + 1] > p
    elif j == matrix.shape[1] - 1:
        return matrix[i - 1, j] > p and matrix[i + 1, j] > p and matrix[i, j - 1] > p
    else:
        return (
            matrix[i - 1, j] > p
            and matrix[i + 1, j] > p
            and matrix[i, j - 1] > p
            and matrix[i, j + 1] > p
        )


res = 0
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if is_low(i, j):
            res += matrix[i, j] + 1
print(res)

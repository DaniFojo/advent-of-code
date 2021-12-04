from pathlib import Path

import numpy as np


def compute_score(k, tensor, seen, number):
    board = seen[k]
    res = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i, j] == 0:
                res += tensor[k, i, j]
    res *= number
    return res


input_file = Path(__file__).parent / "in.txt"

with input_file.open("r") as f:
    input_lines = list(f.readlines())

numbers = [int(i) for i in input_lines[0].strip("\n").split(",")]
input_lines = "".join(input_lines[2:])
boards = input_lines.split("\n\n")[:-1]
tensor = []
for board in boards:
    matrix = []
    for line in board.split("\n"):
        vector = []
        for number in line.split(" "):
            if number:
                vector.append(int(number))
        matrix.append(vector)
    tensor.append(matrix)
tensor = np.array(tensor)
seen = np.zeros_like(tensor)

found = False
for number in numbers:
    if found:
        break
    seen += tensor == number
    for k, board in enumerate(seen):
        for row in range(len(board)):
            if board[row].all():
                found = True
                print(compute_score(k, tensor, seen, number))
        for col in range(len(board[0])):
            if board[:, col].all():
                found = True
                print(compute_score(k, tensor, seen, number))

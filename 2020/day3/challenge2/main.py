from functools import reduce
from pathlib import Path

input_file = Path(__file__).parent / "in.txt"
with input_file.open("r") as f:
    toboggan_map = list(f.readlines())

right_values = [1, 3, 5, 7, 1]
down_values = [1, 1, 1, 1, 2]

res = []
for down, right in zip(down_values, right_values):
    i = 0
    j = 0
    trees = 0
    while i < len(toboggan_map):
        row = toboggan_map[i]
        row = row.strip("\n")
        trees += row[j % len(row)] == "#"
        i += down
        j += right
    res.append(trees)
print(reduce(lambda x, y: x * y, res))

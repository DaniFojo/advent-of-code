from pathlib import Path

import numpy as np

input_file = Path(__file__).parent / "in.txt"

with input_file.open("r") as f:
    vector = np.asarray([int(i) for i in f.read().split(",")], dtype=np.longlong)

values = np.full_like(vector, 1, dtype=np.longlong)

for day in range(256):
    vector -= 1
    new_fish = np.sum(values[vector == -1])
    vector[vector == -1] = 6
    if new_fish:
        vector = np.append(vector, 8)
        values = np.append(values, new_fish)
print(sum(values))

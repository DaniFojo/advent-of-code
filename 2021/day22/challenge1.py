from pathlib import Path
import re
import numpy as np

input_file = Path(__file__).parent / "in.txt"

coordinates = []
is_on = []
with input_file.open("r") as f:
    for line in f.readlines():
        coordinates.append([int(x) for x in re.findall(r"-?\d+", line)])
        is_on.append(line.startswith("on"))

cubes = np.zeros([101, 101, 101], dtype=bool)

for on, coords in zip(is_on, coordinates):
    x1, x2, y1, y2, z1, z2 = coords
    x1, x2, y1, y2, z1, z2 = x1 + 50, x2 + 50, y1 + 50, y2 + 50, z1 + 50, z2 + 50
    cubes[x1 : x2 + 1, y1 : y2 + 1, z1 : z2 + 1] = on
print(cubes.sum())

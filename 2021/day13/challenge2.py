from pathlib import Path

import numpy as np

input_file = Path(__file__).parent / "in.txt"

coords = []
folds = []
with input_file.open("r") as f:
    for line in f.readlines():
        if not line.startswith(("f", "\n")):
            coords.append((int(line.split(",")[0]), int(line.split(",")[1])))
        elif line.startswith("f"):
            if "x" in line:
                folds.append(("x", int(line.split("=")[1])))
            else:
                folds.append(("y", int(line.split("=")[1])))

coords = np.asarray(coords)
for fold in folds:
    ax = 0 if fold[0] == "x" else 1
    coords[coords[:, ax] > fold[1], ax] = (
        2 * fold[1] - coords[coords[:, ax] > fold[1], ax]
    )
letters = np.full((coords[:, 0].max() + 1, coords[:, 1].max() + 1), ".")
for p in coords:
    letters[p[0], p[1]] = "#"

for row in letters.T:
    for letter in row:
        print(letter, end="")
    print("")

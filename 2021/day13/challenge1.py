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
if folds[0][0] == "x":
    coords[coords[:, 0] > folds[0][1], 0] = 2 * folds[0][1] - coords[coords[:, 0] > folds[0][1], 0]

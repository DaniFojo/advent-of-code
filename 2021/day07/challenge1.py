from pathlib import Path

import numpy as np

input_file = Path(__file__).parent / "in.txt"

with input_file.open("r") as f:
    positions = np.asanyarray([int(i) for i in f.read().split(",")])

fuels = [sum(np.abs(positions - i)) for i in range(len(positions))]
print(min(fuels))

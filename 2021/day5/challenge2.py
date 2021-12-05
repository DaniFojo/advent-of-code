from pathlib import Path
import numpy as np
import re

matrix = np.zeros([1000, 1000], dtype=int)
input_file = Path(__file__).parent / "in.txt"

with input_file.open("r") as f:
    for line in f.readlines():
        p = re.compile(r"\d{1,3}")
        x1, y1, x2, y2 = p.findall(line)
        x1, y1, x2, y2 = int(x1) - 1, int(y1) - 1, int(x2) - 1, int(y2) - 1
        if x1 == x2:
            for p in range(min(y1, y2), max(y1, y2)+1):
                matrix[x1, p] += 1
        if y1 == y2:
            for p in range(min(x1, x2), max(x1, x2)+1):
                matrix[p, y1] += 1
        if np.abs(x1 - x2) == np.abs(y1 - y2):
            dx = np.sign(x2 - x1)
            dy = np.sign(y2 - y1)
            for i in range(np.abs(x1 - x2) + 1):
                matrix[x1 + i * dx, y1 + i * dy] += 1

print((matrix > 1).sum())

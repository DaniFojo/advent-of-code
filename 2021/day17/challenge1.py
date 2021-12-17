import math
import re
from pathlib import Path

input_file = Path(__file__).parent / "in.txt"

with input_file.open("r") as f:
    string = f.readline().strip("\n")

x1, x2, y1, y2 = (int(i) for i in re.findall(r"-?\d{1,3}", string))


def simulate(vx, vy):
    x, y = 0, 0
    max_y = 0
    while x < x2 and y > y1:
        x += vx
        y += vy
        max_y = max(y, max_y)
        vx -= 1 if vx > 0 else 0
        vy -= 1
        if (x1 <= x <= x2) and (y1 <= y <= y2):
            return True, max_y
    return False, max_y


vx_min = int((math.sqrt(1 + 8 * x1) - 1) / 2)
vx_max = x2
vy_min = y1
vy_max = -y1

valid = []
for vx in range(vx_min, vx_max + 1):
    for vy in range(vy_min, vy_max + 1):
        ok, max_y = simulate(vx, vy)
        if ok:
            valid.append(max_y)
valid = sorted(valid)
print(valid[-1])

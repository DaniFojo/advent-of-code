from pathlib import Path
import re
from dataclasses import dataclass
from tqdm.contrib import tzip
from collections import Counter

input_file = Path(__file__).parent / "in.txt"
# input_file = Path(__file__).parent / "testcase.txt"

coordinates = []
is_on = []
with input_file.open("r") as f:
    for line in f.readlines():
        coordinates.append([int(x) for x in re.findall(r"-?\d+", line)])
        is_on.append(line.startswith("on"))

@dataclass(frozen=True)
class Cuboid:
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int

    @property
    def size(self):
        return (self.x2-self.x1 + 1) * (self.y2-self.y1 + 1) * (self.z2-self.z1 + 1)


def intersect(cuboid_1, cuboid_2):
    intersection = None
    x_i1 = max(cuboid_1.x1, cuboid_2.x1)
    x_i2 = min(cuboid_1.x2, cuboid_2.x2)
    y_i1 = max(cuboid_1.y1, cuboid_2.y1)
    y_i2 = min(cuboid_1.y2, cuboid_2.y2)
    z_i1 = max(cuboid_1.z1, cuboid_2.z1)
    z_i2 = min(cuboid_1.z2, cuboid_2.z2)
    if (x_i1 <= x_i2) and (y_i1 <= y_i2) and (z_i1 <= z_i2):
        intersection = Cuboid(x_i1, x_i2, y_i1, y_i2, z_i1, z_i2)
    return intersection


class SparseTensor:
    def __init__(self):
        self.cuboids = Counter()

    def set(self, new_cuboid, value):
        new_cubes = Counter()
        for cuboid, value in self.cuboids.items():
            intersection = intersect(cuboid, new_cuboid)
            if intersection:
                new_cubes[intersection] -= value
        if value == 1:
            new_cubes[new_cuboid] += value
        self.cuboids.update(new_cubes)

    def total(self):
        ret = 0
        for c, v in self.cuboids.items():
            ret += c.size * v
        return ret
    
                

tensor = SparseTensor()
for on, coords in tzip(is_on, coordinates):
    x1, x2, y1, y2, z1, z2 = coords
    cuboid = Cuboid(x1, x2, y1, y2, z1, z2)
    tensor.set(cuboid, 1 if on else -1)
print(tensor.total())

from itertools import product
from pathlib import Path

import numpy as np
from tqdm import trange

input_file = Path(__file__).parent / "in.txt"

with input_file.open("r") as f:
    lines = f.readlines()

conversion = np.asarray([1 if c == "#" else 0 for c in lines[0].strip("\n")], dtype=int)

image = np.asarray(
    [[1 if c == "#" else 0 for c in line.strip("\n")] for line in lines[2:]], dtype=int
)


def get_pixel(i, j, image):
    if i < 0 or i >= image.shape[0] or j < 0 or j >= image.shape[0]:
        return 0
    else:
        return image[i, j]


steps = 50
for _ in trange(steps // 2):
    for _ in range(2):
        new_image = np.zeros([image.shape[0] + 8, image.shape[1] + 8], dtype=int)
        for i, j in product(range(new_image.shape[0]), range(new_image.shape[1])):
            i_, j_ = i - 4, j - 4
            pixel = []
            for k, l in product([i_ - 1, i_, i_ + 1], [j_ - 1, j_, j_ + 1]):
                pixel.append(get_pixel(k, l, image))
            num = int("".join(str(p) for p in pixel), 2)
            new_image[i, j] = conversion[num]

        image = new_image.copy()
    image = image[6:-6, 6:-6]

print(image.sum())

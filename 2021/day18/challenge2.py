from __future__ import annotations

import json
from copy import deepcopy
from dataclasses import dataclass
from itertools import product
from pathlib import Path

from tqdm import tqdm


@dataclass
class Pair:

    left: int | Pair
    right: int | Pair

    @property
    def left_depth(self):
        if isinstance(self.left, int):
            return 1
        else:
            return 1 + self.left.depth

    @property
    def right_depth(self):
        if isinstance(self.right, int):
            return 1
        else:
            return 1 + self.right.depth

    @property
    def depth(self):
        return max(self.left_depth, self.right_depth)

    @property
    def magnitude(self):
        return 3 * (
            self.left.magnitude if isinstance(self.left, Pair) else self.left
        ) + 2 * (self.right.magnitude if isinstance(self.right, Pair) else self.right)

    def __add__(self, other):
        return Pair(self, other)

    def __getitem__(self, item):
        try:
            if isinstance(item, tuple) and len(item) == 1:
                item = item[0]
            if item == 0:
                return self.left
            elif item == 1:
                return self.right
            elif isinstance(item, tuple):
                if item[0] == 0:
                    return self.left[item[1:]]
                elif item[0] == 1:
                    return self.right[item[1:]]
        except TypeError:
            pass
        raise IndexError("Wrong indexing")

    def __setitem__(self, key, value):
        if isinstance(key, tuple) and len(key) == 1:
            key = key[0]
        if key == 0:
            self.left = value
        elif key == 1:
            self.right = value
        elif isinstance(key, tuple):
            if key[0] == 0:
                self.left[key[1:]] = value
            elif key[0] == 1:
                self.right[key[1:]] = value

    def __contains__(self, index):
        try:
            self[index]
        except IndexError:
            return False
        return True

    def __repr__(self):
        return f"[{self.left}, {self.right}]"

    def __eq__(self, other):
        if not isinstance(other, Pair):
            return False
        return (self.left == other.left) and (self.right == other.right)

    def iterate_indices(self):
        if isinstance(self.left, int):
            yield (0,)
        else:
            for index in self.left.iterate_indices():
                yield (0, *index)

        if isinstance(self.right, int):
            yield (1,)
        else:
            for index in self.right.iterate_indices():
                yield (1, *index)


def split_number(number):
    if number % 2 == 0:
        return Pair(number // 2, number // 2)
    else:
        return Pair(number // 2, number // 2 + 1)


def parse(chain):
    if isinstance(chain, list):
        return Pair(parse(chain[0]), parse(chain[1]))
    else:
        return chain


def reduce(number):
    split = True
    explode = True
    while split or explode:
        split = False
        explode = False
        all_indices = list(number.iterate_indices())

        # Explode numbers
        if number.depth >= 5:
            explode = True
            for n, index in enumerate(all_indices):
                if len(index) == 5:
                    l = number[index[:-1]].left
                    r = number[index[:-1]].right
                    number[index[:-1]] = 0
                    for index_left in reversed(all_indices[:n]):
                        if index_left in number:
                            number[index_left] += l
                            break
                    for index_right in all_indices[n + 1 :]:
                        if index_right in number:
                            number[index_right] += r
                            break
                    break
        if not explode:
            # Split numbers
            for index in all_indices:
                if number[index] >= 10:
                    number[index] = split_number(number[index])
                    split = True
                    break

    return number


input_file = Path(__file__).parent / "in.txt"

with input_file.open("r") as f:
    number_list = [parse(json.loads(s)) for s in f.readlines()]

n = len(number_list)
magnitudes = []

for i, j in tqdm(product(range(n), range(n)), total=n ** 2):
    if i == j:
        continue

    number = deepcopy(number_list[i]) + deepcopy(number_list[j])
    number = reduce(number)
    magnitudes.append(number.magnitude)

print(sorted(magnitudes)[-1])

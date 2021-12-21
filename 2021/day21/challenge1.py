from itertools import product
from pathlib import Path

input_file = Path(__file__).parent / "in.txt"

with input_file.open("r") as f:
    pos_1 = int(f.readline().split(":")[1])
    pos_2 = int(f.readline().split(":")[1])


class Die:
    def __init__(self):
        self.counter = -1
        self.n = 0

    def roll(self):
        self.counter += 1
        self.n += 1
        self.counter %= 100
        return self.counter + 1


die = Die()
points_1 = 0
points_2 = 0
pos_1 -= 1
pos_2 -= 1

while True:
    pos_1 += die.roll() + die.roll() + die.roll()
    pos_1 %= 10
    points_1 += pos_1 + 1
    if points_1 >= 1000:
        print(die.n * points_2)
        break

    pos_2 += die.roll() + die.roll() + die.roll()
    pos_2 %= 10
    points_2 += pos_2 + 1
    if points_2 >= 1000:
        print(die.n * points_1)
        break

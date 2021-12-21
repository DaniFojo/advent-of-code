from collections import defaultdict
from functools import lru_cache
from itertools import product
from pathlib import Path

input_file = Path(__file__).parent / "in.txt"
with input_file.open("r") as f:
    pos_1 = int(f.readline().split(":")[1])
    pos_2 = int(f.readline().split(":")[1])

probs = defaultdict(int)
for values in product(range(1, 4), repeat=3):
    probs[sum(values)] += 1


@lru_cache(maxsize=None)
def play(positions, points):

    if points[1] >= 21:
        return (0, 1)

    total_wins = [0, 0]
    for value, times in probs.items():
        pos = (positions[0] + value) % 10
        pts = points[0] + (pos + 1)
        wins_this_turn = play((positions[1], pos), (points[1], pts))

        total_wins[0] += wins_this_turn[1] * times
        total_wins[1] += wins_this_turn[0] * times

    return tuple(total_wins)


print(max(play((pos_1 - 1, pos_2 - 1), (0, 0))))

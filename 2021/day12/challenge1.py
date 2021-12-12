from collections import defaultdict
from pathlib import Path

input_file = Path(__file__).parent / "in.txt"

caves = defaultdict(list)
with input_file.open("r") as f:
    for line in f.readlines():
        s, e = line.split("-")
        caves[s].append(e.strip("\n"))
        caves[e.strip("\n")].append(s)


def find_paths(current, used):
    res = 0
    for cave in caves[current]:
        if cave == "end":
            res += 1
        elif cave not in used:
            used_copy = used.copy()
            if cave == cave.lower():
                used_copy.add(cave)
            res += find_paths(cave, used_copy)
    return res


print(find_paths("start", set(["start"])))

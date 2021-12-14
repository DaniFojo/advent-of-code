from collections import Counter, defaultdict
from pathlib import Path
import re

input_file = Path(__file__).parent / "in.txt"

with input_file.open("r") as f:
    lines = list(f.readlines())
    string = lines[0].strip("\n")
    exp = r"[A-Z]{1,2}"
    conversion = {
        re.findall(exp, line)[0]: re.findall(exp, line)[1] for line in lines[2:]
    }

pair_counter = defaultdict(int)
letter_counter = defaultdict(int)
for i in range(len(string) - 1):
    pair = (string[i] + string[i + 1])
    if pair in conversion:
        pair_counter[pair] += 1
    letter_counter[string[i]] += 1
letter_counter[string[-1]] += 1

steps = 40
for _ in range(steps):
    new_pair_counter = defaultdict(int)
    for pair, count in pair_counter.items():
        inserted = conversion[pair]
        letter_counter[inserted] += count
        if (pair[0] + inserted) in conversion:
            new_pair_counter[pair[0] + inserted] += count
        if (inserted + pair[1]) in conversion:
            new_pair_counter[inserted + pair[1]] += count
    pair_counter = new_pair_counter.copy()

counts = sorted([v for k, v in letter_counter.items()])
print(counts[-1] - counts[0])

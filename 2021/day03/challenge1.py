from pathlib import Path

input_file = Path(__file__).parent / "in.txt"

with input_file.open("r") as f:
    input_lines = list(f.readlines())

sums = [0 for _ in input_lines[0].strip("\n")]
for line in input_lines:
    for i, char in enumerate(line.strip("\n")):
        sums[i] += int(char)

most_common = [s > (len(input_lines) // 2) for s in sums]
epsilon = int("".join(["1" if c else "0" for c in most_common]), 2)
gamma = int("".join(["0" if c else "1" for c in most_common]), 2)
print(epsilon * gamma)

from pathlib import Path

input_file = Path(__file__).parent / "in.txt"
with input_file.open("r") as f:
    toboggan_map = list(f.readlines())

i = 0
trees = 0
for row in toboggan_map:
    row = row.strip("\n")
    trees += row[i % len(row)] == "#"
    i += 3
print(trees)

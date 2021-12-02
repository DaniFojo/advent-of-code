from pathlib import Path


def is_valid(line):
    n_min = int(line.split("-")[0])
    n_max = int(line.split("-")[1].split(" ")[0])
    letter = line.split(" ")[1].split(":")[0]
    text = line.split(" ")[2]
    count = text.count(letter)
    return n_min <= count <= n_max


input_file = Path(__file__).parent / "in.txt"
with input_file.open("r") as f:
    res = 0
    for line in f.readlines():
        if line:
            if is_valid(line):
                res += 1

print(res)

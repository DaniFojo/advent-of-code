from pathlib import Path
import itertools

input_file = Path(__file__).parent / "in.txt"

with input_file.open("r") as f:
    lines = f.readlines()

input_digits = [line.split("|")[0].split(" ")[:-1] for line in lines]
output_digits = [line.strip("\n").split("|")[1].split(" ")[1:] for line in lines]

res = 0
for output in itertools.chain(*output_digits):
    if len(output) in {2, 4, 3, 7}:
        res += 1

print(res)

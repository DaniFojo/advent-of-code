from pathlib import Path

input_file = Path(__file__).parent / "in.txt"

with input_file.open("r") as f:
    input_string = f.read()

numbers = [int(n) for n in input_string.split("\n") if n]
found = False
for i, n in enumerate(numbers):
    if found:
        break
    for m in numbers[i + 1:]:
        if n + m == 2020:
            print(n * m)
            found = True
            break

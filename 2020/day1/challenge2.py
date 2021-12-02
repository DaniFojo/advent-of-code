from pathlib import Path

input_file = Path(__file__).parent / "in.txt"

with input_file.open("r") as f:
    input_string = f.read()

numbers = [int(n) for n in input_string.split("\n") if n]
found = False
for i, n in enumerate(numbers):
    if found:
        break
    for j, m in enumerate(numbers[i + 1 :]):
        if found:
            break
        for k, p in enumerate(numbers[i + j + 2 :]):
            if n + m + p == 2020:
                print(n * m * p)
                found = True
                break

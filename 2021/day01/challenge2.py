from pathlib import Path

input_file = Path(__file__).parent / "in.txt"

with input_file.open("r") as f:
    input_string = f.read()

numbers = [int(n) for n in input_string.split("\n") if n]

window_sums = [sum(x) for x in zip(numbers[:-2], numbers[1:-1], numbers[2:])]
print(sum(window_sums[i] < window_sums[i + 1] for i in range(len(window_sums) - 1)))

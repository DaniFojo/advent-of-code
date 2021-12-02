from pathlib import Path

input_file = Path(__file__).parent / "in.txt"

with input_file.open("r") as f:
    input_string = f.read()

numbers = [int(n) for n in input_string.split("\n") if n]
last_depth = numbers[0]
output = 0
for number in numbers[1:]:
    if number > last_depth:
        output += 1
    last_depth = number
print(output)

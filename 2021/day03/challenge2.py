from pathlib import Path


def find_number(input_lines, is_oxygen):
    for i in range(len(input_lines[0])):
        position_sum = sum(int(line[i]) for line in input_lines)
        most_common_1 = position_sum >= len(input_lines) / 2
        if is_oxygen:
            input_lines = [
                line for line in input_lines if (bool(int(line[i]))) == most_common_1
            ]
        else:
            input_lines = [
                line for line in input_lines if (bool(int(line[i]))) != most_common_1
            ]
        if len(input_lines) == 1:
            return input_lines[0]


input_file = Path(__file__).parent / "in.txt"

with input_file.open("r") as f:
    input_lines = list(line.strip("\n") for line in f.readlines())

input_lines_copy = input_lines.copy()
oxygen = find_number(input_lines, True)
co2 = find_number(input_lines_copy, False)

oxygen = int(oxygen, 2)
co2 = int(co2, 2)
print(oxygen * co2)

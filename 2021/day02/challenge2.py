from pathlib import Path

input_file = Path(__file__).parent / "in.txt"
with input_file.open("r") as f:
    depth = 0
    forward = 0
    aim = 0
    for line in f.readlines():
        if line:
            instruction, number = line.split(" ")[0], int(line.split(" ")[1])
            if instruction == "forward":
                forward += number
                depth += number * aim
            elif instruction == "down":
                aim += number
            else:
                aim -= number

print(depth * forward)

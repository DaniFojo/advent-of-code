from pathlib import Path

input_file = Path(__file__).parent / "in.txt"
with input_file.open("r") as f:
    depth = 0
    forward = 0
    for line in f.readlines():
        if line:
            instruction, number = line.split(" ")[0], int(line.split(" ")[1])
            if instruction == "forward":
                forward += number
            elif instruction == "down":
                depth += number
            else:
                depth -= number

print(depth * forward)

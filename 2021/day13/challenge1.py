from pathlib import Path

input_file = Path(__file__).parent / "in.txt"

read = []
with input_file.open("r") as f:
    for line in f.readlines():
        if not line.startswith("f"):
            read.append(line.split(",")[0], line.split(",")[1].strip("\n"))

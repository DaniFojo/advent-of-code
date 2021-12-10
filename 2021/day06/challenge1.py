from pathlib import Path

input_file = Path(__file__).parent / "in.txt"

with input_file.open("r") as f:
    vector = [int(i) for i in f.read().split(",")]

for day in range(256):
    print(day)
    for i in range(len(vector)):
        if vector[i] == 0:
            vector[i] = 6
            vector.append(8)
        else:
            vector[i] -= 1
print(len(vector))

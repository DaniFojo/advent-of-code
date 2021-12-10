from pathlib import Path

input_file = Path(__file__).parent / "in.txt"

# ): 3 points.
# ]: 57 points.
# }: 1197 points.
# >: 25137 points.
points = {")": 3, "]": 57, "}": 1197, ">": 25137}

res = 0
with input_file.open("r") as f:
    for line in f.readlines():
        q = []
        for c in line:
            if c == "\n":
                break
            if c in "([{<":
                q.append(c)
            else:
                last = q.pop()
                if not (
                    (c == ")" and last == "(")
                    or (c == "]" and last == "[")
                    or (c == "}" and last == "{")
                    or (c == ">" and last == "<")
                ):
                    res += points[c]
                    break

print(res)

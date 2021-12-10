from pathlib import Path

input_file = Path(__file__).parent / "in.txt"

# ): 1 point.
# ]: 2 points.
# }: 3 points.
# >: 4 points.
points = {"(": 1, "[": 2, "{": 3, "<": 4}

res_list = []
with input_file.open("r") as f:
    for line in f.readlines():
        corrupted = False
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
                    corrupted = True
                    break
        if not corrupted:
            res = 0
            for missing in reversed(q):
                res *= 5
                res += points[missing]
            res_list.append(res)

print(res_list[len(res_list) // 2])

from collections import defaultdict
from pathlib import Path

input_file = Path(__file__).parent / "in.txt"

with input_file.open("r") as f:
    lines = f.readlines()

input_digits = [line.split("|")[0].split(" ")[:-1] for line in lines]
output_digits = [line.strip("\n").split("|")[1].split(" ")[1:] for line in lines]

used_segments = {
    "a": [0, 2, 3, 5, 6, 7, 8, 9],
    "b": [0, 4, 5, 6, 8, 9],
    "c": [0, 1, 2, 3, 4, 7, 8, 9],
    "d": [2, 3, 4, 5, 6, 8, 9],
    "e": [0, 2, 6, 8],
    "f": [0, 1, 3, 4, 5, 6, 7, 8, 9],
    "g": [0, 2, 3, 5, 6, 8, 9],
}
reverse_used_segments = {
    i: set(x for x in used_segments if i in used_segments[x]) for i in range(10)
}

possible_digits_by_len = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [0, 6, 9], 7: [8]}
res_sum = 0
for digits, output in zip(input_digits, output_digits):
    digit_to_letters = {}
    letter_count = defaultdict(int)
    for digit in digits:
        if len(digit) == 3:
            digit_to_letters[7] = set(digit)
        if len(digit) == 2:
            digit_to_letters[1] = set(digit)
        if len(digit) == 4:
            digit_to_letters[4] = set(digit)
        if len(digit) == 7:
            digit_to_letters[8] = set(digit)
        for d in digit:
            letter_count[d] += 1

    final_mapping = {}

    # a appears in 7 and not in 1
    final_mapping["a"] = digit_to_letters[7].difference(digit_to_letters[1])
    final_mapping["a"] = next(iter(final_mapping["a"]))

    # Use letter counts for the rest of the mapping
    for k, v in letter_count.items():
        if v == 4:
            final_mapping["e"] = k
        if v == 6:
            final_mapping["b"] = k
        if v == 9:
            final_mapping["f"] = k
        if v == 8:
            if k != final_mapping["a"]:
                final_mapping["c"] = k
        if v == 7:
            if k in digit_to_letters[4]:
                final_mapping["d"] = k
            else:
                final_mapping["g"] = k

    reverse_final_mapping = {v: k for k, v in final_mapping.items()}
    res = []
    for o in output:
        real = set(reverse_final_mapping[i] for i in o)
        for i in range(10):
            if set(reverse_used_segments[i]) == real:
                res.append(i)
    res_sum += int("".join(str(r) for r in res))
print(res_sum)

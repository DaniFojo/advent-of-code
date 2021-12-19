import re
from pathlib import Path
from scipy.spatial.transform import Rotation
import numpy as np
from collections import Counter

input_file = Path(__file__).parent / "in.txt"

with input_file.open("r") as f:
    exp = r"(?:-?\d{1,3},-?\d{1,3},-?\d{1,3}\n?)+"
    scans = re.findall(exp, f.read())

scans = [s.strip("\n").split("\n") for s in scans]
for scan in scans:
    for j, probe in enumerate(scan):
        scan[j] = np.array([int(i) for i in probe.split(",")])

scans = [np.stack(s) for s in scans]

rotations = [
    Rotation.from_euler("ZX", [0, 0], degrees=True),
    Rotation.from_euler("ZX", [0, 90], degrees=True),
    Rotation.from_euler("ZX", [0, 180], degrees=True),
    Rotation.from_euler("ZX", [0, 270], degrees=True),
    Rotation.from_euler("ZX", [90, 0], degrees=True),
    Rotation.from_euler("ZX", [90, 90], degrees=True),
    Rotation.from_euler("ZX", [90, 180], degrees=True),
    Rotation.from_euler("ZX", [90, 270], degrees=True),
    Rotation.from_euler("ZX", [180, 0], degrees=True),
    Rotation.from_euler("ZX", [180, 90], degrees=True),
    Rotation.from_euler("ZX", [180, 180], degrees=True),
    Rotation.from_euler("ZX", [180, 270], degrees=True),
    Rotation.from_euler("ZX", [270, 0], degrees=True),
    Rotation.from_euler("ZX", [270, 90], degrees=True),
    Rotation.from_euler("ZX", [270, 180], degrees=True),
    Rotation.from_euler("ZX", [270, 270], degrees=True),
    Rotation.from_euler("YX", [90, 0], degrees=True),
    Rotation.from_euler("YX", [90, 90], degrees=True),
    Rotation.from_euler("YX", [90, 180], degrees=True),
    Rotation.from_euler("YX", [90, 270], degrees=True),
    Rotation.from_euler("YX", [270, 0], degrees=True),
    Rotation.from_euler("YX", [270, 90], degrees=True),
    Rotation.from_euler("YX", [270, 180], degrees=True),
    Rotation.from_euler("YX", [270, 270], degrees=True),
]

probes = set(tuple(p) for p in scans[0])
found = [False for _ in range(len(scans))]
found[0] = True
while not all(found):
    for i in range(1, len(scans)):
        if not found[i]:
            for r in rotations: 
                difference_counts = Counter()
                rotated_scan = r.apply(scans[i])
                rotated_scan = np.round(rotated_scan).astype(int)
                for probe in probes:
                    differences = rotated_scan - probe
                    difference_counts.update(tuple(d) for d in differences)
                diff, count = difference_counts.most_common(1)[0]
                if count >= 12:
                    # Correct orientation
                    probes.update(set(tuple(r) for r in rotated_scan - diff))
                    found[i] = True

print(len(probes))

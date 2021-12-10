#!/usr/bin/env python3

import sys

with open("day2.input", "r") as fp:
    input = fp.read()

x = 0
y = 0
aim = 0

for line in input.split("\n"):
    direction, distance = line.split()
    if direction == "forward":
        x += int(distance)
        y += aim*int(distance)
    elif direction == "up":
        aim -= int(distance)
    elif direction == "down":
        aim += int(distance)
    else:
        print("Unknown direction.", file=sys.stderr)

print(f"X: {x}, Y: {y}")
print(f"Product: {x*y}")
#!/usr/bin/env python3

import numpy as np

def binaryToDecimal(a):
    return np.sum(a * 2**np.arange(len(a))[::-1])

with open("day3.input", "r") as fp:
    input = fp.read()

input = np.array([list(i) for i in input.split("\n")]).astype(np.int32)

# 1
gamma = np.median(input, axis=0)
epsilon = 1-gamma

print(f"Gamma: {gamma}, Epsilon: {epsilon}")
print(f"Product: {binaryToDecimal(gamma)*binaryToDecimal(epsilon)}")

# 2 
input_temp = input.copy()

# Oxygen
for i in range(input.shape[1]):
    if input.shape[0] == 1:
        break
    input = input[input[:, i] == np.ceil(np.median(input[:, i])), :]

print(f"Oxygen: {input}")
oxygen = binaryToDecimal(input.ravel())

# CO2
input = input_temp.copy()
for i in range(input.shape[1]):
    if input.shape[0] == 1:
        break
    input = input[input[:, i] == 1-np.ceil(np.median(input[:, i])), :]

print(f"CO2: {input}")
co2 = binaryToDecimal(input.ravel())

print(f"Product: {oxygen*co2}")
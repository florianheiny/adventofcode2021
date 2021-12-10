#!/usr/bin/env python3

import numpy as np

def numberOfIncreases(a):
    return np.sum(np.diff(a) > 0)

# 1 
input = np.fromfile("day1.input", sep="\n")
print(numberOfIncreases(input))

# 2
input2 = np.convolve(input, np.array([1,1,1]), mode="valid")
print(numberOfIncreases(input2))
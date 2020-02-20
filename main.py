#!/bin/env python3

import sys
import os
from src.Importer import Importer
import random
import zipfile

def zipdir():
    zipf = zipfile.ZipFile('outputs/output.zip', 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk("src/"):
        for file in files:
            zipf.write(os.path.join(root, file))
    zipf.write("main.py")

# Update input file names (these are the practice round ones...)
inputs = {
    "a": "a_example.txt",
    "b": "b_small.txt",
    "c": "c_medium.txt",
    "d": "d_quite_big.txt",
    "e": "e_also_big.txt"
}

inSet = ""
inFile = ""
if len(sys.argv) >= 2 and sys.argv[1] in inputs.keys():
    inSet = sys.argv[1]
    inFile = "inputs/" + inputs[inSet]
else:
    print("Please specify a input set from the following:")
    for i in inputs.keys():
        print(str(i), end=" ")
    sys.exit()

importer = Importer(inFile)
M, N, slices = importer.import_data_set()

# M is maximum number of pizza slices to order

# N is number of different pizza types there are i.e. len(slices)

# slices is a list of how many slices a type of pizza has
# index 0 contains the number of slices for pizza type 0 (S_0)

# Let's get started

# List of types to order
types = [] # ...

# Number of different types of pizza to order
K = len(types)

# Sanity check
totalSlices = 0
for i in types:
    totalSlices += slices[i]

if totalSlices > M:
    print("ERROR: Something has gone wrong. Total slices has exceeded M.")

f = open("outputs/"+inSet+".txt", "w")
f.write(str(K) + "\n")
f.write(" ".join(map(str, types)) + "\n")
f.close()

zipdir()

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
data = importer.import_data_set()

# Let's get started

# [Insert processing here...]

f = open("outputs/"+inSet+".txt", "w")
# [Write output to file here...]
f.close()

zipdir()

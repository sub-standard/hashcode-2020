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
    "b": "b_read_on.txt",
    "c": "c_incunabula.txt",
    "d": "d_tough_choices.txt",
    "e": "e_so_many_books.txt",
    "f": "f_libraries_of_the_world.txt"
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
B, L, D, bookScores, libraries = importer.import_data_set()

# B: number of books ie len(bookScores)
# L: number of libraries ie len(libraries)
# D: number of days
# bookScores: list of scores of each book where the index is the book ID
# libraries: list of tuples of:
    # N: number of books in library
    # T: number of days to finish library signup
    # M: number of books shippable from library per day
    # books: list of book IDs in the library (where book ID is the index of the book score in bookScores)

# Let's get started

# [Insert processing here...]

f = open("outputs/"+inSet+".txt", "w")
# [Write output to file here...]
f.close()

# zipdir()

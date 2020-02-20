#!/bin/env python3

import sys
import os
from src.Importer import Importer
from src.Book import Book
from src.Library import Library
from src.sort_libraries import sort_libraries
import random
import zipfile
from src.optimizer import *


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

number_of_books, number_of_libraries, days, books, libraries = importer.import_data_to_objects()

print(f"Days: {days}, Libraries: {len(libraries)}, Books: {len(books)}")

solution = []

sorted_libraries = None

t = 0
imported_books = []
while (t < days and len(libraries) > 0):
    print(f"Day {t} | Libraries: {len(libraries)}")

    # first_library = first_library_optimizer(number_of_books, number_of_libraries, days, books, libraries)

    # sort libraries based on maximum score achievable in time remaining
    if t == 0 or probablistic_sort(t, days):
        sorted_libraries = sort_libraries(libraries, days, t, imported_books)

    # pick top library
    chosen_library = sorted_libraries[0]["library"]
    chosen_books = sorted_libraries[0]["books"]

    print(f"Chose library: L#{chosen_library.id}")

    # remove chosen library from selection
    try:
        libraries.remove(chosen_library)
    except:
        pass

    # mark books as imported
    imported_books += chosen_books

    for library in libraries:
        library.books = [
            book for book in library.books if book not in chosen_books]

    # add library to solution along with sorted books in order of score
    solution.append((chosen_library, chosen_books))

    # increment current time to next possible setup
    t += chosen_library.sign_up_time
### END SOLUTION ###

### EXPORT SOLUTION ###
f = open("outputs/"+inSet+".txt", "w")

solution = [(lib, books) for (lib, books) in solution if len(books) > 0]

f.write(f"{len(solution)}\n")  # <number of libraries>
for library, chosen_books in solution:
    if len(chosen_books) == 0:
        raise "ERROR: found a library with no books while outputting"

    # <library ID> <number of books to scan>
    f.write(f"{library.id} {len(chosen_books)}\n")

    # <[book ids] in order of score>
    sorted_books = sorted(chosen_books, key=lambda book: book.score)

    f.write(" ".join(map(str, map(Book.get_id, sorted_books))) + "\n")
f.close()
### END EXPORT SOLUTION ###

zipdir()

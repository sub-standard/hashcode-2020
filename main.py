#!/bin/env python3

import sys
import os
from math import ceil
from src.Importer import Importer
from src.Book import Book
from src.Library import Library
from src.sort_libraries import sort_libraries
import random
import zipfile
from src.optimizer import *

LOG_NORMAL = 0
LOG_DEBUG = 1
LOG_TRACE = 2
LOG_LEVELS = ['normal', 'debug', 'trace']

log_level_env = os.getenv('HC_LOG_LEVEL', 'normal')

try:
    log_level = LOG_LEVELS.index(log_level_env)
except ValueError:
    log_level = LOG_NORMAL

def zipdir():
    zipf = zipfile.ZipFile('outputs/output.zip', 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk("src/"):
        for file in files:
            zipf.write(os.path.join(root, file))
    zipf.write("main.py")

def log_normal(msg):
    if log_level >= LOG_NORMAL:
        print(msg)

def log_debug(msg):
    if log_level >= LOG_DEBUG:
        print(msg)

def log_trace(msg):
    if log_level >= LOG_TRACE:
        print(msg)

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

log_normal("Started importing...")
importer = Importer(inFile)

number_of_books, number_of_libraries, days, books, libraries = importer.import_data_to_objects()
log_normal("Done importing")

print(f"Days: {days}, Libraries: {len(libraries)}, Books: {len(books)}")

log_normal("Started processing...")
solution = []

# sorted_libraries = None

t = 0
imported_books = []
while (t < days and len(libraries) > 0):
    log_debug(f"Day {t} | Libraries: {len(libraries)}")

    # first_library = first_library_optimizer(number_of_books, number_of_libraries, days, books, libraries)

    # sort libraries based on maximum score achievable in time remaining
    # if t == 0 or probablistic_sort(t, days):
    sorted_libraries = sort_libraries(libraries, days, t, imported_books)

    # pick top library
    chosen_library = sorted_libraries[0]["library"]
    chosen_books = sorted_libraries[0]["books"]

    log_debug(f"Chose library: {chosen_library} with {len(chosen_books)} chosen books")

    # remove chosen library from selection
    libraries.remove(chosen_library)
    # try:
    # except:
    #     pass

    # mark books as imported
    imported_books += chosen_books

    for library in libraries:
        library.books = [
            book for book in library.books if book not in chosen_books]

    # add library to solution along with sorted books in order of score
    solution.append((chosen_library, chosen_books))

    # increment current time to next possible setup
    t += chosen_library.sign_up_time

    libraries = [
        library for library in libraries if library.sign_up_time + t < days]
### END SOLUTION ###
log_normal("Done processing")

log_normal("Started exporting...")
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
log_normal("Done exporting")

log_normal("Started visualising...")
### VISUALISE SOLUTION ###
v = open("outputs/visual/"+inSet+".txt", "w")
v.write("|" + ' '*days + "|\n")
time = 0
for library, chosen_books in solution:
    days_for_books = ceil(len(chosen_books)/library.book_throughput)
    v.write('|' + ' '*time + 'X'*library.sign_up_time + '-'*days_for_books + ' '*(days-time-library.sign_up_time-days_for_books) + "|\n")
    time += library.sign_up_time
v.close()
### END VISUALISE SOLUTION ###
log_normal("Done visualising")

zipdir()

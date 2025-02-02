import os.path
from src.Book import Book
from src.Library import Library

class Importer:
    def __init__(self, filename : str) -> None:
        self.filename: str = filename

    # Read the input from the input file
    def import_data_set(self):
        if os.path.isfile(self.filename):
            with open(self.filename, 'r') as file:
                content = file.readlines()

                line1 = content[0].strip()
                parts = line1.split(" ")
                B = int(parts[0])
                L = int(parts[1])
                D = int(parts[2])

                line2 = content[1].strip()
                parts2 = line2.split(" ")
                bookScores = []
                for part in parts2:
                    bookScores.append(int(part))

                libraries = []
                for i in range(0, L):
                    libLine1 = content[2+i*2].strip()
                    libParts = libLine1.split(" ")

                    N = int(libParts[0])
                    T = int(libParts[1])
                    M = int(libParts[2])

                    books = []

                    libLine2 = content[2 + i*2 + 1].strip()
                    books = list(map(int, libLine2.split(" ")))

                    libraries.append((N, T, M, books))

                return B, L, D, bookScores, libraries
        else:
            print("Error: File not found")
            raise FileNotFoundError

    def import_data_to_objects(self):
        B, L, D, bookScores, libraries = self.import_data_set()

        outBooks = []
        for i in range(0, len(bookScores)):
            outBooks.append(Book(i, bookScores[i]))

        outLibraries = []
        for i in range(0, len(libraries)):
            N, T, M, books = libraries[i]

            libBooks = []
            for b in books:
                libBooks.append(outBooks[b])

            outLibraries.append(Library(i, libBooks, T, M))

        return B, L, D, outBooks, outLibraries

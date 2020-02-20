import math as m


def first_library_optimizer(no_of_book, no_of_lib, day, books_score, libraries_books):
    # Number of days to process (min), number of books important
    # -log(sign_up_time/100)*const + log(books_per_day/no_of_books)*const + uniqueness_score

    alpha = 10
    beta = 10

    for library_book in libraries_books:
        no_of_books, sign_up_time, books_per_day, books = library_book

        heuristic_score = (-m.log(sign_up_time/100) * alpha) + (m.log(books_per_day/no_of_books) * beta) +

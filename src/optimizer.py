import math as m
import random


def uniqueness_score():
    return []

def first_library_optimizer(no_of_book, no_of_lib, day, books_score, libraries_books):
    # Number of days to process (min), number of books important
    # -log(sign_up_time/100)*const + log(books_per_day/no_of_books)*const + uniqueness_score

    alpha, beta, gamma = 10, 10, 0.01  # some arbitrary numbers

    best_heuristic = 0
    best_library_index = 0

    for index in range(len(libraries_books)):
        no_of_books, sign_up_time, books_per_day, books = libraries_books[index]

        heuristic_score = (-m.log(sign_up_time * gamma) * alpha) + \
            (m.log(books_per_day / no_of_books) * beta)  # + uniqueness_score()

        if heuristic_score > best_heuristic:
            best_library_index = index

    return libraries_books[best_library_index]


def probablistic_sort(current_time_step, sign_up_time):
    rate = random.randrange(0, 1)
    return bool(rate > m.log(1) / 100)

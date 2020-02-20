from src.Book import Book

# number_of_books, number_of_libraries, days, book_scores, libraries


def sort_libraries(libraries, days, current_day, imported_books):
    results = []

    for library in libraries:
        books = library.books

        if not books:
            continue

        number_of_books_to_take = (
            library.book_throughput * (days - current_day - library.sign_up_time))
        scannable_books = books[:number_of_books_to_take]

        weight = 0
        for book in scannable_books:
            weight += book.score

        results.append({
            "library": library,
            "weight": weight,
            "books": scannable_books
        })

    sorted_results = sorted(results, key=lambda r: r['weight'])

    return [sorted_result for sorted_result in sorted_results]

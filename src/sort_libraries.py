# number_of_books, number_of_libraries, days, book_scores, libraries


def sort_libraries(libraries, days, current_day, imported_books):
    results = []

    for library in libraries:
        books = []

        for book in library.books:
            if book not in imported_books:
                books.append(book)

        sorted_books = sorted(books, key=lambda book: book.score)
        number_of_books_to_take = (
            library.book_throughput * (days - current_day - library.sign_up_time))
        scannable_books = sorted_books[:number_of_books_to_take]
        weight = sum(map(lambda book: book.score, scannable_books))

        results.append({
            "library": library,
            "weight": weight,
            "books": scannable_books
        })

    sorted_results = sorted(results, key=lambda r: r['weight'])

    return [sorted_result for sorted_result in sorted_results]

# number_of_books, number_of_libraries, days, book_scores, libraries


def sort_libraries(libraries, days, current_day, imported_books):
    results = []

    for library in libraries:
        total_book_score = 0

        for book in library.books:
            if not book in imported_books:
                total_book_score += book.score

        weight = total_book_score / \
            (library.book_throughput * (days - current_day - library.sign_up_time))

        results.append({
            "library": library,
            "weight": weight
        })

    sorted_results = sorted(results, key=lambda r: r['weight'])

    return [sorted_result['library'] for sorted_result in sorted_results]

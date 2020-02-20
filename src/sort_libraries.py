# number_of_books, number_of_libraries, days, book_scores, libraries


def sort_libraries(libraries, days, current_day, imported_books):
    results = []

    for library in libraries:
        total_book_score = [book.score for book in library.books]

        weight = total_book_score / \
            (library.book_throughput * (days - current_day - library.sign_up_time))

        results.append({
            "library": library,
            "weight": weight
        })

    sorted_results = results.sort(lambda result: result["weight"])

    return [sorted_result['library'] for sorted_result in sorted_results]

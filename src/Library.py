class Library():
    def __init__(self, id, books, sign_up_time, book_throughput):
        self.id = id
        self.books = books
        self.sign_up_time = sign_up_time
        self.book_throughput = book_throughput
        self.number_of_books = len(books)

    def __str__(self):
        # return f"L#{self.id} [{[str(b) for b in self.books]}]"
        return f"L#{self.id} ({self.number_of_books} books)"

    def __eq__(self, other):
        return self.id == other.id

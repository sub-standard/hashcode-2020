class Library():
    def __init__(self, id, books, sign_up_time, book_throughput):
        self.id = id
        self.books = books
        self.sign_up_time = sign_up_time
        self.book_throughput = book_throughput

    def __str__(self):
        return f"L#{self.id} [{[str(b) for b in self.books]}]"

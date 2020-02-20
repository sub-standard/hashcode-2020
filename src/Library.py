from src.Book import Book


class Library():
    def __init__(self, id, books, sign_up_time, book_throughput):
        self.id = id
        self.initial_books = sorted(books, key=Book.get_score)
        self.books = self.initial_books
        self.sign_up_time = sign_up_time
        self.book_throughput = book_throughput
        self.number_of_books = len(books)
        self.score = None

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return score

    def __str__(self):
        # return f"L#{self.id} [{[str(b) for b in self.books]}]"
        return f"L#{self.id} ({self.number_of_books} books, {self.sign_up_time} sign up time, {self.book_throughput} books/day)"

    def __eq__(self, other):
        return self.id == other.id

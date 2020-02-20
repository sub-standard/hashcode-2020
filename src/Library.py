class Library():
    def __init__(self, id, books):
        self.id = id
        self.books = books

    def __str__(self):
        return f"L#{self.id} [{[str(b) for b in self.books]}]"

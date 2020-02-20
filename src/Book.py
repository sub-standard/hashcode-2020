class Book():
    def __init__(self, id, score):
        self.id = id
        self.score = score

    def __str__(self):
        return f"B#{str(self.id)} ({str(self.score)})"

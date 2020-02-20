class Book():
    def __init__(self, id, score):
        self.id = id
        self.score = score

    def get_id(self):
        return self.id

    def get_score(self):
        return self.score

    def __str__(self):
        return f"B#{str(self.id)} ({str(self.score)})"

    def __eq__(self, other):
        return self.id == other.id

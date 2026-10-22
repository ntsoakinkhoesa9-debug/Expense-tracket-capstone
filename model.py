class Expense:
    """Model class - Separation of Concerns (UJ Q1)"""
    def __init__(self, title, amount, category):
        self.title = title
        self.amount = float(amount)
        self.category = category

    def to_dict(self):
        return {
            "title": self.title,
            "amount": self.amount,
            "category": self.category
        }

    @staticmethod
    def from_dict(data):
        return Expense(data["title"], data["amount"], data["category"])

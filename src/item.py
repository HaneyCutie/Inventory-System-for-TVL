class Item:
    def __init__(self, name, category, quantity, threshold=1):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.threshold = threshold

    def __str__(self):
        return f"{self.name} ({self.category}) - Qty: {self.quantity}"
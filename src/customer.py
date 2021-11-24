class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.stomach = []

    def reduce_wallet(self, drink):
        self.wallet -= drink.price

    def add_to_stomach(self, drink):
        self.stomach.append(drink.name)

    def stomach_count(self):
        return len(self.stomach)

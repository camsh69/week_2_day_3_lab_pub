class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.stomach = []
        self.drink = []
        self.age = age

    def reduce_wallet(self, drink):
        self.wallet -= drink.price

    def add_to_stomach(self, drink):
        self.stomach.append(drink.name)

    def bought_drink(self, drink):
        self.drink.append(drink.name)

    def drink_count(self):
        return len(self.drink)

    def stomach_count(self):
        return len(self.stomach)

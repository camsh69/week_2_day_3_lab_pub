class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, drink):
        self.till += drink.price

    def check_stock(self, drink):
        for item in self.drinks:
            if item["name"] == drink:
                return item["amount"]
        return None

    def add_drinks(self, drink, amount):
        stock = {
            "name": drink.name,
            "amount": amount
        }
        self.drinks.append(stock)

    def remove_drink(self, drink):
        for item in self.drinks:
            if item["name"] == drink.name:
                item["amount"] -= 1

class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, drink):
        self.till += drink.price

    def check_stock(self, drink_name):
        for drink in self.drinks:
            if drink["name"] == drink_name:
                return drink["amount"]
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

    def sell_drink(self, customer, drink):
        if customer.drunkeness <= 7:
            if self.check_stock(drink.name) != None:
                if customer.age < 18 and drink.alcoholic_status == True:
                    return "Sorry, you're too young for booze"
                else:
                    customer.reduce_wallet(drink)
                    customer.bought_drink(drink)
                    self.increase_till(drink)
                    self.remove_drink(drink)
            return "Sorry out of stock"
        return "Sorry, you're too drunk"

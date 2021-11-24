import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer


class TestPub(unittest.TestCase):

    def setUp(self):
        drink_1 = Drink("lager", 4.00, True)
        self.pub = Pub("The Prancing Pony", 100.00, drink_1)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_till_when_drink_sold(self):
        drink = Drink("stout", 4.00, True)
        self.pub.increase_till(drink)
        self.assertEqual(104.00, self.pub.till)

    def test_check_stock_is_empty(self):
        self.assertEqual(None, self.pub.check_stock("lager"))

    def test_check_stock_amount_when_adding_drink(self):
        drink = Drink("stout", 4.00, True)
        self.pub.add_drinks(drink, 5)
        self.assertEqual(5, self.pub.check_stock(drink.name))

    def test_check_stock_amount_when_removing_drink(self):
        drink = Drink("stout", 4.00, True)
        self.pub.add_drinks(drink, 5)
        self.pub.remove_drink(drink)
        self.assertEqual(4, self.pub.check_stock(drink.name))

    def test_sell_drink_to_customer(self):
        customer = Customer("Joe Bloggs", 50.00)
        drink = Drink("stout", 4.00, True)
        self.pub.add_drinks(drink, 5)
        self.pub.sell_drink(customer, drink)
        self.assertEqual(46.00, customer.wallet)
        self.assertEqual(1, customer.drink_count())
        self.assertEqual(104.00, self.pub.till)
        self.assertEqual(4, self.pub.check_stock(drink.name))

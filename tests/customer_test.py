import unittest
from src.customer import Customer
from src.drink import Drink


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Joe Bloggs", 50.00)

    def test_reduce_wallet_if_drink_bought(self):
        drink = Drink("IPA", 3.00, True)
        self.customer.reduce_wallet(drink)
        self.assertEqual(47.00, self.customer.wallet)

    def test_is_stomach_empty(self):
        self.assertEqual(0, self.customer.stomach_count())

    def test_add_one_drink_to_stomach(self):
        drink = Drink("coca-cola",2.00, False)
        self.customer.add_to_stomach(drink)
        self.assertEqual(1,self.customer.stomach_count())

    def test_add_more_drinks_to_stomach(self):
        drink_1 = Drink("Coca-cola", 2.00, False)
        drink_2 = Drink("Sprite", 2.00, False)
        self.customer.add_to_stomach(drink_1)
        self.customer.add_to_stomach(drink_2)
        self.assertEqual(2, self.customer.stomach_count())


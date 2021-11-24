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

    # def test_number_of_drinks_in_stomach(self):
    #     drink = Drink("coca-cola", 2.00, False)

    # def test_add_drink_to_stomach(self):
    #     drink = Drink("coca-cola",2.00, False)
    #     self.customer.add_to_stomach(drink)
    #     self.assertEqual(,self.customer.stomach)

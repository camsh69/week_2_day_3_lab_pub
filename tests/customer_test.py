import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Joe Bloggs", 50.00)

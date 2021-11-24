import unittest
from src.drink import Drink


class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("lager", 4.00, True, 3)

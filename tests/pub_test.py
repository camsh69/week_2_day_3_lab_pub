import unittest
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    def setUp(self):
        drink_1 = Drink("lager", 4.00, True)
        self.pub = Pub("The Prancing Pony", 100.00, drink_1)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)    


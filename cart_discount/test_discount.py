import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    
    # TODO more unit tests here. Each test should test one scenario

    # test with a list of 2 prices
    def test_list_of_two_prices(self):
        prices = [15, 7]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))
    

    # test with a list 1 price
        
    def test_list_of_one_price(self):
        prices = [15]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))
    

    # a list of 6 prices ?
    
    def test_list_of_six_prices(self):
        prices = [1, 2.62, 3, 4, 5, 6]
        expected_discount = 1
        self.assertEqual(expected_discount, discount(prices))
    
    def test_list_of_strings(self):
        prices = ['1', '2', '87']
        # TODO what -do- we expect?
        # Input into webforms is usually a string, as opposed to int or float
        self.fail('Finish test for list of strings') # TODO remove this when code when test is finished

    # what other data might this function have to deal with?
        # Probably floating point numbers, though error handling for non-number strings would be good. 
    
    # remember a function has no control over how it is used
    # it may be called with any data - and it should be able to handle whatever data it gets appropriately 

if __name__ == '__main__':
    unittest.main()
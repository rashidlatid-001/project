import unittest
import service
import math_utils

class TestIntegration(unittest.TestCase):

    def test_total_price(self):
        self.assertEqual(service.calculate_total_price(100, 3), 300)

    def test_discount_workflow(self):
        result = service.apply_discount(service.calculate_total_price(200, 2), 50)
        self.assertEqual(result, 350)   
    def test_add_function(self):
        self.assertEqual(math_utils.add(5, 7), 12)
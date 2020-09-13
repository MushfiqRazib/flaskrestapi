import unittest
import datetime
from app.main import db
from app.main.service.computation_service import FibonacciStrategy
from app.test.basetest import BaseTestCase


class TestFibService(BaseTestCase):

    def test_fib_result_type(self):
        fb = FibonacciStrategy()
        num = 11
        result = fb.fib(num)
        self.assertTrue(isinstance(result, int))

    def test_fib_result(self):
        fb = FibonacciStrategy()
        num = 6
        result = fb.fib(num)
        self.assertEqual(result, 13, "Should be 13")

    def test_fib_compute_result(self):
        fb = FibonacciStrategy()
        num = 11
        result = fb.compute_algorithm(num)
        self.assertEqual(result, [[3, 8], [3, 3, 5], [2, 2, 2, 5], [2, 3, 3, 3], [2, 2, 2, 2, 3]], "Should be same")


if __name__ == '__main__':
    unittest.main()
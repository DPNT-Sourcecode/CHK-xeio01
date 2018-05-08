import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_illegal_input_returns_-one(self):
        self.assertEqual(
            -1,
            checkout('K')
        )

    def test_promo_applied_to_a(self):
        self.assertEqual(
            260,
            checkout('AAAAAA')  # ?? 6A or 6 As?
        )

    def test_promo_applied_to_b(self):
        # self.fail()

    def test_promo_applied_to_a_and_b(self):
        # self.fail()
    
    def test_valid_input_returns_correct_amount(self):
        # self.fail()


if __name__ == '__main__':
    unittest.main()

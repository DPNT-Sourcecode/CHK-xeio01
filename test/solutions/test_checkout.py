import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_illegal_input_returns_minus_one(self):
        self.assertEqual(
            -1,
            checkout('K')
        )

    def test_promo_applied_to_a(self):
        self.assertEqual(
            260,
            checkout('AAAAAA')
        )

    def test_promo_applied_to_b(self):
        self.assertEqual(
            90,
            checkout('BB')
        )

    def test_promo_applied_to_a_and_b(self):
        self.assertEqual(
            175,
            checkout('AAABB')
        )
    
    def test_valid_input_returns_correct_amount(self):
        self.assertEqual(
            130,
            checkout('ABCDD')
        )


if __name__ == '__main__':
    unittest.main()

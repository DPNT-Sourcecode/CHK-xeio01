import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_illegal_input_returns_minus_one(self):
        self.assertEqual(
            -1,
            checkout('1')
        )

    def test_promo_applied_to_a(self):
        self.assertEqual(
            250,
            checkout('AAAAAA')
        )

    def test_promo_applied_to_b(self):
        self.assertEqual(
            90,
            checkout('BBBB')
        )

    def test_promo_applied_to_a_and_b(self):
        self.assertEqual(
            175,
            checkout('AAABB')
        )

    def test_promo_applied_to_e_and_b(self):
        self.assertEqual(
            110,
            checkout('EEBB')
        )

    def test_multiple_promo_applied_to_a(self):
        self.assertEqual(
            330,
            checkout('AAAAAAAA')
        )

    def test_multiple_promo_applied_to_b(self):
        self.assertEqual(
            125,
            checkout('EEBBB')
        )

    def test_promo_applied_to_F(self):
        self.assertEqual(
            20,
            checkout('FFF')
        )
    
    def test_promo_applied_to_f_sanely(self):
        self.assertEqual(
            30,
            checkout('FFFF')
        )

    # should change the tests to instead pass in a test config with loads
    # of items and promos of the expected format
    # but maybe later
    
    def test_valid_input_returns_correct_amount(self):
        self.assertEqual(
            130,
            checkout('ABCDD')
        )

    def test_t_returns_correct_amount(self):
        self.assertEqual(
            20,
            checkout('T')
        )
    
    def test_x_returns_correct_amount(self):
        self.assertEqual(
            17,
            checkout('X')
        )

    def test_y_returns_correct_amount(self):
        self.assertEqual(
            20,
            checkout('Y')
        )
    
    def test_z_returns_correct_amount(self):
        self.assertEqual(
            21,
            checkout('Z')
        )

    def test_weird_promo_returns_correct_amount(self):
        self.assertEqual(
            45,
            checkout('STX')
        )

    def test_weird_promo_returns_correct_amount_two(self):
        self.assertEqual(
            90,
            checkout('STXSTX')
        )

if __name__ == '__main__':
    unittest.main()

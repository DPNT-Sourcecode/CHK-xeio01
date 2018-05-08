import unittest

from lib.solutions.hello import hello


class TestHello(unittest.TestCase):
    def test_hello_outputs_correct_name(self):
        result = hello('John')
        
        self.assertEqual('Hello, John!', result)


if __name__ == '__main__':
    unittest.main()

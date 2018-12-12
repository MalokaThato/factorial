import unittest
import factorial

class testfact(unittest.TestCase):
    def test_fact(self):
        result = factorial.factorial_num(4)

        self.assertEqual(result,24)

if __name__ == "__main__":
    unittest.main()

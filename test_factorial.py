import unittest
import factorial

class testfact(unittest.TestCase):
    def test_fact(self):
        result = factorial.factorial_num((input("Enter the number you would like to get's factorial: ")))

        self.assertEqual(result,24)

if __name__ == "__main__":
    unittest.main()

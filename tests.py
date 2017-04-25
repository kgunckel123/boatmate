import unittest
from model import schedule_optimize


class TestModel(unittest.TestCase):

    def test_base_case(self):
        weights=[10, 10, 10, 10, 14, 14, 5, 5, 6, 6, 6, 6, 5, 5, 5, 1, 1, 1, 1, 11, 11, 11, 9, 9, 13, 13, 13]
        length=len(weights)
        print(length)
        val = schedule_optimize(weights)
        expected = {}  # put expected here
        self.assertEqual(val, expected)


class TestGUI(unittest.TestCase):

    def test_functions(self):
        pass


if __name__ == "__main__":
    unittest.main()
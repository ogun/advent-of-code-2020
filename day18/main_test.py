import unittest

import day18.main as main


class TestAnswers(unittest.TestCase):
    def test_part1(self):
        actual = main.part1()
        expected = 8298263963837
        self.assertEqual(actual, expected)

    def test_part2(self):
        actual = main.part2()
        expected = 145575710203332
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

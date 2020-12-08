import unittest

import day03.main as main


class TestAnswers(unittest.TestCase):
    def test_part1(self):
        actual = main.part1()
        expected = 250
        self.assertEqual(actual, expected)

    def test_part2(self):
        actual = main.part2()
        expected = 1592662500
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

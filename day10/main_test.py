import unittest

import day10.main as main


class TestAnswers(unittest.TestCase):
    def test_part1(self):
        actual = main.part1()
        expected = 2112
        self.assertEqual(actual, expected)

    def test_part2(self):
        actual = main.part2()
        expected = 3022415986688
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

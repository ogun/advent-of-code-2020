import unittest

import main


class TestAnswers(unittest.TestCase):
    def test_day1_part1(self):
        actual = main.day1_part1()
        expected = 928896
        self.assertEqual(actual, expected)

    def test_day1_part2(self):
        actual = main.day1_part2()
        expected = 295668576
        self.assertEqual(actual, expected)

    def test_day2_part1(self):
        actual = main.day2_part1()
        expected = 600
        self.assertEqual(actual, expected)

    def test_day2_part2(self):
        actual = main.day2_part2()
        expected = 245
        self.assertEqual(actual, expected)

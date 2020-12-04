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

    def test_day3_part1(self):
        actual = main.day3_part1()
        expected = 250
        self.assertEqual(actual, expected)

    def test_day3_part2(self):
        actual = main.day3_part2()
        expected = 1592662500
        self.assertEqual(actual, expected)

    def test_day4_part1(self):
        actual = main.day4_part1()
        expected = 222
        self.assertEqual(actual, expected)

    def test_day4_part2(self):
        actual = main.day4_part2()
        expected = 140
        self.assertEqual(actual, expected)

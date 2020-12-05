import unittest

import main


class TestAnswers(unittest.TestCase):
    def test_day01_part1(self):
        actual = main.day01_part1()
        expected = 928896
        self.assertEqual(actual, expected)

    def test_day01_part2(self):
        actual = main.day01_part2()
        expected = 295668576
        self.assertEqual(actual, expected)

    def test_day02_part1(self):
        actual = main.day02_part1()
        expected = 600
        self.assertEqual(actual, expected)

    def test_day02_part2(self):
        actual = main.day02_part2()
        expected = 245
        self.assertEqual(actual, expected)

    def test_day03_part1(self):
        actual = main.day03_part1()
        expected = 250
        self.assertEqual(actual, expected)

    def test_day03_part2(self):
        actual = main.day03_part2()
        expected = 1592662500
        self.assertEqual(actual, expected)

    def test_day04_part1(self):
        actual = main.day04_part1()
        expected = 222
        self.assertEqual(actual, expected)

    def test_day04_part2(self):
        actual = main.day04_part2()
        expected = 140
        self.assertEqual(actual, expected)

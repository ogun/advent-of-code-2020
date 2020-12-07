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

    def test_day05_part1(self):
        actual = main.day05_part1()
        expected = 991
        self.assertEqual(actual, expected)

    def test_day05_part2(self):
        actual = main.day05_part2()
        expected = 534
        self.assertEqual(actual, expected)

    def test_day06_part1(self):
        actual = main.day06_part1()
        expected = 6625
        self.assertEqual(actual, expected)

    def test_day06_part2(self):
        actual = main.day06_part2()
        expected = 3360
        self.assertEqual(actual, expected)

    def test_day07_part1(self):
        actual = main.day07_part1()
        expected = 254
        self.assertEqual(actual, expected)

    def test_day07_part2(self):
        actual = main.day07_part2()
        expected = 6006
        self.assertEqual(actual, expected)

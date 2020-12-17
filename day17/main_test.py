import unittest

import day17.main as main


class TestAnswers(unittest.TestCase):
    def test_part1(self):
        actual = main.part1()
        expected = 232
        self.assertEqual(actual, expected)

    def test_part2(self):
        actual = main.part2()
        expected = 1620
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

import unittest

import day13.main as main


class TestAnswers(unittest.TestCase):
    def test_part1(self):
        actual = main.part1()
        expected = 246
        self.assertEqual(actual, expected)

    def test_part2(self):
        actual = main.part2()
        expected = 939490236001473
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

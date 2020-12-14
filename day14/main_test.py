import unittest

import day14.main as main


class TestAnswers(unittest.TestCase):
    def test_part1(self):
        actual = main.part1()
        expected = 9967721333886
        self.assertEqual(actual, expected)

    def test_part2(self):
        actual = main.part2()
        expected = 4355897790573
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

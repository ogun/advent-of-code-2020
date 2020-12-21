import unittest

import day21.main as main


class TestAnswers(unittest.TestCase):
    def test_part1(self):
        actual = main.part1()
        expected = 2614
        self.assertEqual(actual, expected)

    def test_part2(self):
        actual = main.part2()
        expected = "qhvz,kbcpn,fzsl,mjzrj,bmj,mksmf,gptv,kgkrhg"
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

import unittest

from cut.mathclass import Math


class MathTests(unittest.TestCase):

    def test_add(self):
        num1 = 2
        num2 = 3

        math = Math(num1, num2)

        self.assertEqual(2 + 3, math.add())

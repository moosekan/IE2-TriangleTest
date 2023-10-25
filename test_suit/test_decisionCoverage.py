import unittest
from isTriangle import Triangle


class TriangleTest(unittest.TestCase):

    def test_invalid1(self):
        self.assertEqual(Triangle.classify(0, 1, 2), Triangle.Type.INVALID)

    def test_invalid2(self):
        actual1 = Triangle.classify(5, 4, 10)
        expected1 = Triangle.Type.INVALID
        self.assertEqual(actual1, expected1)

    def test_invalid3(self):
        actual2 = Triangle.classify(5, 5, 11)
        expected2 = Triangle.Type.INVALID
        self.assertEqual(actual2, expected2)


        # actual4 = Triangle.classify(11, 5, 5)
        # expected4 = Triangle.Type.INVALID
        # self.assertEqual(actual4, expected4)

    def test1(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test_isosceles(self):
        actual = Triangle.classify(5, 5, 4)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
        actual1 = Triangle.classify(5, 4, 5)
        expected1 = Triangle.Type.ISOSCELES
        self.assertEqual(actual1, expected1)
        actual2 = Triangle.classify(4, 5, 5)
        expected2 = Triangle.Type.ISOSCELES
        self.assertEqual(actual2, expected2)

    def test_scalene(self):
        actual = Triangle.classify(9, 7, 5)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

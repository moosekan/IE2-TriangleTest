import unittest
import inspect
import types
from isTriangle import Triangle


class TriangleTest(unittest.TestCase):
    INVALID = 0
    SCALENE = 1
    EQUILATERAL = 2
    ISOSCELES = 3


    def test_invalid1(self):
        self.assertEqual(Triangle.classify(0, 0, 0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, 0, -1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(-1, 2, 0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, -1, 0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, 0,0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(3,0,0),  Triangle.Type.INVALID)

    def test_invalid2(self):
        self.assertEqual(Triangle.classify(10, -2, 9), Triangle.Type.INVALID)  # done
        self.assertEqual(Triangle.classify(9, 10, -2), Triangle.Type.INVALID)  # done
        self.assertEqual(Triangle.classify(-2, 9, 10), Triangle.Type.INVALID)  # done
        self.assertEqual(Triangle.classify(5, 4, 10), Triangle.Type.INVALID)  # done
        # for line 34
        self.assertEqual(Triangle.classify(5, 6, 11), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(5, 11, 6), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(11, 5, 6), Triangle.Type.INVALID)

    def test_invalid3(self):
        self.assertEqual(Triangle.classify(5, 5, 11), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(5, 11, 5), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(11, 5, 5), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(-1, 5, 5), Triangle.Type.INVALID)  # done
        self.assertEqual(Triangle.classify(5, -1, 5), Triangle.Type.INVALID)  # done
        self.assertEqual(Triangle.classify(5, 5, -1), Triangle.Type.INVALID)  # done

    def test_equilateral(self):
        self.assertEqual(Triangle.classify(10, 10, 10), Triangle.Type.EQUILATERAL)

    def test_isosceles(self):
        self.assertEqual(Triangle.classify(5, 5, 6), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(3, 3, 5), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(5, 6, 5), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(6, 5, 5), Triangle.Type.ISOSCELES)

    def test_scalene(self):
        self.assertEqual(Triangle.classify(5, 10, 6), Triangle.Type.SCALENE)  # done
        self.assertEqual(Triangle.classify(5, 6, 10), Triangle.Type.SCALENE)  # done
        self.assertEqual(Triangle.classify(6, 5, 10), Triangle.Type.SCALENE)  # done

    def test_enum(self):
        self.assertEqual(Triangle.classify(5, 10, 6).value, 1)
        self.assertEqual(Triangle.classify(6, 5, 5).value, 3)
        self.assertEqual(Triangle.classify(10, 10, 10).value, 2)
        self.assertEqual(Triangle.classify(0, 0, 0).value, 0)
    def test_zero_condition(self):
        self.assertEqual(Triangle.classify(1, 1, 0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 0, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(0, 1, 1), Triangle.Type.INVALID)
    def test_static(self):
        static_methods = [name for name, method in Triangle.__dict__.items() if isinstance(method, staticmethod)]
        number_of_static_methods = len(static_methods)
        self.assertEqual(number_of_static_methods, 1)
    def test_invalid_62(self):
        self.assertEqual(Triangle.classify(5, 5, 10), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(5, 10, 5), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(10, 5, 5), Triangle.Type.INVALID)

if __name__ == '__main__':
    unittest.main()
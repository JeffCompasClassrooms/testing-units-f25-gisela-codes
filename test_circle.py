import unittest
from circle import Circle
import math

circle = Circle(4)
class test_circle(unittest.TestCase):
    def test_getRadius(self):
        self.assertEqual(circle.getRadius(), 4)
   
    def test_setRadius1(self):
        self.assertEqual(circle.setRadius(0), True)

    def test_setRadius2(self):
        self.assertEqual(circle.setRadius(-0.1), False)

    def test_getArea(self):
        self.assertEqual(circle.getArea(), math.pi * 4 * 4)

    def test_getArea2(self):
        circle.setRadius(2)
        self.assertEqual(circle.getArea(), math.pi * 2 * 2)

    def test_getCircumference(self):
        circle.setRadius(4)

        self.assertEqual(circle.getCircumference(), 2 *  math.pi * 4)
    
    def test_getCircumference2(self):
        circle = Circle(2)
        self.assertEqual(circle.getCircumference(), 2 *  math.pi * 2)

if __name__ == "__main__":
    unittest.main()

#coverage run -m unittest discover
#coverage report -m
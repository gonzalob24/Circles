import unittest
from check_circle_inside_another_circle import circle_inside_another_circle


class Test_Circles(unittest.TestCase):

    def test_r1_equals_r2(self):
        self.assertEqual(circle_inside_another_circle(
            (0, 0), 4, (1, 1), 4), False, "Should be False")

    def test_same_center(self):
        self.assertEqual(circle_inside_another_circle(
            (0, 0), 4, (0, 0), 9), True, "Should be True")

    def test_same_center2(self):
        self.assertEqual(circle_inside_another_circle(
            (0, 0), 9, (0, 0), 8.9), True, "Should be True")

    def test_opposite_locations(self):
        self.assertEqual(circle_inside_another_circle(
            (-5, 3), 2, (5, 3), 2), False, "Should be False")

    def test_3(self):
        self.assertEqual(circle_inside_another_circle(
            (6, 7), 1, (8, 5), 3), False, "Should be False")

    def test_4(self):
        self.assertEqual(circle_inside_another_circle(
            (-5, -3), 2, (-2, -2), 5), False, "Should be False")


if __name__ == "__main__":
    unittest.main()

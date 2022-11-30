
import unittest
from multiple import mul_viky

class TestMultiplyByThree(unittest.TestCase):

	def test_multiply_by_three(self):
		self.assertEqual(mul_viky.mul_by_same_number(5), 9)

unittest.main()
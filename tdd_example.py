#!/usr/bin/env python

import unittest

def calculate_addition_string(expression):
	return ''

class TestAdditionMethod(unittest.TestCase):
	def test_only_zero(self):
		self.assertEqual(calculate_addition_string("0"),0)

if __name__ == '__main__':
	unittest.main()

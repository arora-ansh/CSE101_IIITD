# Name : Ansh Arora
# Roll No : 2019022
# Group : 4

import unittest
from a1 import changeBase

# TEST cases should cover the different boundary cases.

class testpoint(unittest.TestCase):
	
	def test_change_base(self):
		
		self.assertEqual(changeBase(1,"MYR","MYR","2019-01-13"), 1.0)
		self.assertEqual(changeBase(1,"AUD","AUD","2015-01-13"), 1.0)
		self.assertEqual(changeBase(1,"EUR","EUR","2019-08-07"), 1.0)
		self.assertAlmostEqual(changeBase(1, "EUR", "CAD", "2017-08-18"), 1.4908, delta = 0.1)
		self.assertAlmostEqual(changeBase(1, "EUR", "INR", "2018-10-24"), 83.3255, delta = 0.1)
		self.assertAlmostEqual(changeBase(1, "CAD", "MYR", "2019-09-10"), 3.168, delta = 0.1)
		self.assertAlmostEqual(changeBase(1, "USD", "INR", "2017-01-13"), 68.163, delta = 0.1)
		self.assertAlmostEqual(changeBase(1, "GBP", "EUR", "2019-06-13"), 1.1243, delta = 0.1)
		self.assertAlmostEqual(changeBase(1, "GBP", "HKD", "2019-10-01"), 9.6059, delta = 0.1)
		self.assertAlmostEqual(changeBase(1, "INR", "JPY", "2016-02-29"), 1.6555, delta = 0.1)


		# these are just sample values. You have to add testcases (and edit these) for various dates.
		# (don't use the current date as the json would keep changing every 4 minutes)
		# you have to hard-code the 2nd parameter of assertEquals by calculating it manually
		# on a particular date and checking whether your changeBase function returns the same
		# value or not.




if __name__=='__main__':
	unittest.main()

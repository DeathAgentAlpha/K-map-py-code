# CSE 101 - IP HW2
# K-Map Minimization Test Cases
# Name: HARSH KUMAR
# Roll Number: 2018285
# Section: B
# Group: 6
# Date: 17/10/2018
import unittest
from HW2_2018285 import minFunc

class testpoint(unittest.TestCase):
	def test_minFunc(self):
		self.assertEqual(minFunc(4,'(1,3,7,11,15) d (0,2,5)'),'w\'z+yz')
		self.assertEqual(minFunc(3,'(1,3,7) d (0,2,5)'),'y')
		self.assertEqual(minFunc(2,'(1,3) d -'),'x')
		self.assertEqual(minFunc(1,'(0) d -'),'w\'')
		self.assertEqual(minFunc(4,'(0,1,2,3,4,5,6,7,8,9,12,13) d -'),'w\'+y\'')
		self.assertEqual(minFunc(4,'(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14) d (15)'),'1')
		self.assertEqual(minFunc(3,'() d -'),'0')
if __name__=='__main__':
	unittest.main()
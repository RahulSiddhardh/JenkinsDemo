#! /usr/bin/python 

import unittest

from Program1 import summation 

class TestSum(unittest.TestCase):
      def test_list_int(self):
            data = [2, 6]
            result = summation(data)
            self.assertEqual(result, 8)
      
if __name__ == "__main__":
      unittest.main()

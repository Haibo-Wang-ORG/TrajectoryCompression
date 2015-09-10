import unittest
from dp import DouglasPeucker

class DPTestCase(unittest.TestCase):
    """Tests for 'dp.py'"""
    
    _Q = [[-3, 0],
         [-2, 1],
         [0, -2],
         [2, 1],
         [3, 0]
         ]
    
    _dp = DouglasPeucker()
    
    def test_is_uncompressed_douglas_peucker(self):
        """Does the algorithm compress no data when the delta is 0?"""
        self.assertEqual(range(len(self._Q)), self._dp._douglas_peucker(self._Q, 0, len(self._Q)-1, 0))
        
    def test_is_maximum_compressed_douglas_peucker(self):
        """Does the algorithm compress all data except the two ends when the delta is +infinity?"""
        self.assertEqual([0,len(self._Q)-1], self._dp._douglas_peucker(self._Q, 0, len(self._Q)-1, float('inf')))
        
    def test_is_partially_compressed_douglas_peucker(self):
        """Does the algorithm partially compress the data when the delta is 1.5?"""
        self.assertEqual([0,2,len(self._Q)-1], self._dp._douglas_peucker(self._Q, 0, len(self._Q)-1, 1.5))
        
if __name__ == '__main__':
    unittest.main()
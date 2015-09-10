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
        self.assertEqual(range(5), self._dp._douglas_peucker(self._Q, 0, len(self._Q)-1, 0))
        
if __name__ == '__main__':
    unittest.main()
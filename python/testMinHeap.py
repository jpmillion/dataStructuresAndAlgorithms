import unittest
from minHeap import MinHeap

class TestMinHeap(unittest.TestCase):

    def testBuildHeap(self):
        arr = [9,5,8,1,3,6,7,11,-8,-9,15]
        actual = [-9,9,6,-8,5,8,7,11,1,3,15]
        minHeap = MinHeap(arr)
        self.assertEquals(actual, minHeap.heap)


if __name__ == '__main__':
    unittest.main()
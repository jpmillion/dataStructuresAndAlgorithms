import unittest
from minHeap import MinHeap

class TestMinHeap(unittest.TestCase):

    def testBuildHeap(self):
        arr = [9,5,8,1,3,6,7,11,-8,-9,15]
        actual = [-9,-8,6,1,3,8,7,11,9,5,15]
        minHeap = MinHeap(arr)
        self.assertEqual(actual, minHeap.heap)

    def testRemove(self):
        arr = [9,5,8,1,3,6,7,11,-8,-9,15]
        actual = [-8,1,6,9,3,8,7,11,15,5]
        minHeap = MinHeap(arr)
        minElement = minHeap.remove()
        self.assertEqual(actual, minHeap.heap)
        self.assertEqual(-9, minElement)


if __name__ == '__main__':
    unittest.main()
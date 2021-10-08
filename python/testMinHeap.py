import unittest
from minHeap import MinHeap

class TestMinHeap(unittest.TestCase):

    def testBuildHeap(self):
        arr = [9,5,8,1,3,6,7,11,-8,-9,15]
        actual = [-9,-8,6,1,3,8,7,11,9,5,15]
        minHeap = MinHeap(arr)
        self.assertEqual(actual, minHeap.heap, 'should build heap')

    def testRemove(self):
        arr = [9,5,8,1,3,6,7,11,-8,-9,15]
        actual = [-8,1,6,9,3,8,7,11,15,5]
        minHeap = MinHeap(arr)
        minElement = minHeap.remove()
        self.assertEqual(actual, minHeap.heap, 'should remove minElement')
        self.assertEqual(-9, minElement)

    def testInsert(self):
        arr = [9,5,8,1,3,6,7,11,-8,-9,15]
        actual = [-9,-8,4,1,3,6,7,11,9,5,15,8]
        minHeap = MinHeap(arr)
        minHeap.insert(4)
        self.assertEqual(actual, minHeap.heap, 'should insert element')



if __name__ == '__main__':
    unittest.main()
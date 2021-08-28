import unittest
import sort

class TestSort(unittest.TestCase):

    def testMergeSort(self):
        arr = [20, -10, -30, 30, 40, 10, 0, -50, 5]

        sort.mergeSort(arr)
        self.assertListEqual([-50, -30, -10, 0, 5, 10, 20, 30, 40], arr, 'should sort array')
    

if __name__ == '__main__':
    unittest.main()
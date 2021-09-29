import unittest
import search

class TestSearch(unittest.TestCase):

    def testDepthFirstSearch(self):
        class Node:
            def __init__(self, value):
                self.value = value
                self.children = []

        root = Node(0)

        for i in range(1, 10):
            child = Node(i)
            root.children.append(child)
            for j in range((i*10), (i*10)+10):
                grandChild = Node(j)
                child.children.append(grandChild)
                for k in range((j*10), (j*10)+10):
                    greatGrandChild = Node(k)
                    grandChild.children.append(greatGrandChild)

        # self.assertEqual(True, search.depthFirstSearch(root, 0))
        # self.assertEqual(False, search.depthFirstSearch(root, 11111), 'Should be false')
        
        # self.assertEqual(True, search.depthFirstSearch(root, 0), 'Should be false')
        # self.assertEqual(True, search.depthFirstSearch(root, 8), 'Should be false')
        # self.assertEqual(True, search.depthFirstSearch(root, 33), 'Should be false')
        self.assertEqual(True, search.depthFirstSearch(root, 105), 'Should be false')


if __name__ == '__main__':
    unittest.main()
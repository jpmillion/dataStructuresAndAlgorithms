class MinHeap:

    def __init__(self, arr):
        self.heap = arr
        self.buildHeap()

    def buildHeap(self):
        heap = self.heap
        firstParentIdx = (len(heap)) // 2 - 1
        for i in reversed(range(0, firstParentIdx + 1)):
            self.siftDown(i)
        
    
    def siftDown(self, parentIdx):
        heap = self.heap
        firstChildIdx = parentIdx * 2 + 1
        secondChildIdx = parentIdx * 2 + 2 if parentIdx * 2 + 2 < len(heap) else -1 

        # if parent has one child or first child is less than second child, 
        # the first child will be the parentIdx to compare; else the second child
        idxToCompare = firstChildIdx if secondChildIdx == -1 or heap[firstChildIdx] < heap[secondChildIdx] else secondChildIdx

        if heap[idxToCompare] < heap[parentIdx]:
            heap[idxToCompare], heap[parentIdx] = heap[parentIdx], heap[idxToCompare]

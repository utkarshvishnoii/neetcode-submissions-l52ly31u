class MedianFinder:

    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap,num)

    def findMedian(self) -> float:
        n = len(self.heap)
        self.heap.sort()
        if n%2 == 0:
            first = (n//2 - 1)
            second = first + 1
            return (self.heap[first]+self.heap[second])/2
        else:
            return self.heap[n//2]

[1,2,3]



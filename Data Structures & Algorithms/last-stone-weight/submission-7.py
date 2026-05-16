import heapq as h
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            h.heappush(heap,-s)

        while len(heap)>1:
            first = -h.heappop(heap)
            second = -h.heappop(heap)

            if first == second:
                continue
            else:
                diff = abs(first-second)
                h.heappush(heap,-diff)
        return -h.heappop(heap) if heap else 0


import heapq as h
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            h.heappush(heap,-s)

        while heap:
            first = -h.heappop(heap)
            if heap:
                second = -h.heappop(heap)
            else:
                return abs(first)

            if first == second:
                continue
            else:
                diff = abs(first-second)
                h.heappush(heap,-diff)
        return 0


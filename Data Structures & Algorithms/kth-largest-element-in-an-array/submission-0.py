import heapq as h
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return h.nlargest(k,nums)[-1]
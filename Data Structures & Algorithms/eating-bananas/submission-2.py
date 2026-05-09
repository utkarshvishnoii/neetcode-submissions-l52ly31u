class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        res = max(piles)
        while l <= r:
            m = (l+r)//2
            sum = 0
            for p in piles:
                sum+=math.ceil(p/m)
            if sum > h:
                l = m+1
            else:
                res = m
                r = m-1
        return res



[1,2,3,4]
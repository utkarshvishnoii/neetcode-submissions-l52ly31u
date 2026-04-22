class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        res = r

        while l <= r:
            m = (l+r) //  2
            sum = 0
            for p in piles:
                sum+= math.ceil(float(p)/m)
            if sum <= h:
                r = m-1
                res = m
            else:
                l= m+1
        return res


# piles = [ 1,4,3,2]

# [ 1 2 3 4]
#   l     r                                                         r

# l = 1, r = 2
# h = 9
# res = 
# m = 2
# sum 1+2+2+1

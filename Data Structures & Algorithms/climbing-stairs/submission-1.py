class Solution:
    def climbStairs(self, n: int) -> int:
        one,two = 1,1

        for i in range(n-1):
            one,two = one+two,one
        return one

# n = 5
# 8  5  3  2  1  1
# 0  1  2  3  4  5
#             o  t
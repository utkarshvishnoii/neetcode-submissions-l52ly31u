class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numS = set(nums)
        res = 0
        for n in nums:
            curr = n
            count = 0

            while curr in numS:
                count+=1
                curr+=1
            res = max(res,count)
        return res

# [1,2,10,3]
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        cnt = 1
        res = 0
        for i,a in enumerate(nums):
            if a not in numSet:
                numSet.add(a)
                cnt = 1
                while a+1 in nums:
                    numSet.add(a+1)
                    a+=1
                    cnt+=1
                res = max(res,cnt)
        return res


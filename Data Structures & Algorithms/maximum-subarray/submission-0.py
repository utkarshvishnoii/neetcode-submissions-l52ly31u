class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = min(nums)
        for i in range(len(nums)):
            currSum = 0
            for j in range(i,len(nums)):
                currSum = currSum + nums[j]
                res = max(res,currSum)

        return res
        
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxRes = nums[0]
        currSum = 0
        for n in nums:
            if currSum<0:
                currSum = 0
            currSum+=n
            maxRes = max(maxRes,currSum)
        return maxRes


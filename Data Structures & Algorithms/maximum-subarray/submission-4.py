# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         maxRes = nums[0]
#         currSum = 0
#         for n in nums:
#             if n<0:
#                 currSum = 0
#             currSum+=n
#             maxRes = max(maxRes,currSum)
#         return maxRes
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub
    


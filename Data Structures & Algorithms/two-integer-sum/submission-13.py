class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = defaultdict()

        for i,a in enumerate(nums):
            diff = target - a

            if diff in numSet:
                return [numSet[diff],i]
            numSet[a] = i  
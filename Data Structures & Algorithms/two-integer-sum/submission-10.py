class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countN = defaultdict(int)

        for i,n in enumerate(nums):
            diff = target - n
            if diff in countN:
                return [countN[diff],i]
            countN[n] = i


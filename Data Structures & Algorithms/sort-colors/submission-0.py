class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = 0, len(nums)-1
        p = 0

        while p <=r:
            if nums[p] == 0:
                nums[p],nums[l] = nums[l],nums[p]
                l+=1
            elif nums[p] == 2:
                nums[p],nums[r] = nums[r],nums[p]
                r-=1
                p-=1
            p+=1
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        rec = defaultdict(int)
        for n in nums:
            if n in rec:
                return True
            else:
                rec[n] +=1
        return False

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        

# loop around nums [1,2,3,3]
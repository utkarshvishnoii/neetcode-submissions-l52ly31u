class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for i in numSet:
            if (i-1) in numSet:
                continue
            else:
                largest = 1
                j=i+1
                while j in numSet:
                    largest = largest+1
                    j+=1
                longest = max(longest,largest)
        return longest
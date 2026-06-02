class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = []
        for n in nums:
            if n != val:
                c.append(n)
        for i in range(len(c)):
            nums[i] = c[i]
        return len(c)
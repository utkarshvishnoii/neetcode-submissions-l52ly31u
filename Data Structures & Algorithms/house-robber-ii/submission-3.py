class Solution:
    def rob(self, nums: List[int]) -> int:
        nums1 = nums[:len(nums)-1]
        nums2 = nums[1:]

        def robber(arr):
            one,two = 0,0

            for n in arr:
                temp = max(two,n+one)
                one = two
                two = temp
            return two
        return max(nums[0],robber(nums1),robber(nums2))


# [2, 3, 4, 2, 5]
#  2  3  6  6  11
#          o  t
# one=3
# two= 6
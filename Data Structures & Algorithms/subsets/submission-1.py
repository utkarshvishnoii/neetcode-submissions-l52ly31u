class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res  = []
        subset = []
        def dfs(i):
            if i >=len(nums):
                return res.append(subset.copy())
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        dfs(0)
        return res

# idx-> 0,1,2
# nums=[1,2,3]
#       i
#           j
# res = [[],[1],[1,2],[]]
# temp = [1,2,3]
# i = 0
# j = 2

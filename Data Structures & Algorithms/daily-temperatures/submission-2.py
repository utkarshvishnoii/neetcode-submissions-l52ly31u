class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res =[0]*len(temperatures)
        stack = []

        for i,a in enumerate(temperatures):
            while stack and a > stack[-1][0]:
                temp,idx = stack.pop()
                res[idx] = i-idx
            stack.append((a,i))
        return res



# [30,38,30,36,35,40,28]
#                  i

# [(38,1)(36,3)]
# res = [1,0,1,0,1,0,0]
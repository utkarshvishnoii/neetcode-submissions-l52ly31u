class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res =[]
        for l in range(len(temperatures)):
            r=l+1
            while r<len(temperatures) and temperatures[l] >= temperatures[r]  :
                r+=1
            diff = r-l if r<len(temperatures) else 0
            res.append(diff)
        return res

#        l
# [30,38,30,36,35,40,28]
#            r

# res = [1,4,]
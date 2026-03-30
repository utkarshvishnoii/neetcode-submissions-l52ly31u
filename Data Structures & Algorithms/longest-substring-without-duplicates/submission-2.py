class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        distinctS = set()
        for r in range(len(s)):
            while s[r] in distinctS:
                distinctS.remove(s[l])
                l+=1
            distinctS.add(s[r])
            res = max(res,r-l+1)
        return res
        # [zxyzab]
        # distinct= (z,x,y,)
        # count = 3
        #res = 1
        #  lrrr
        #  remove from set if already present
        #  increment l by 1
        #  count = (r-l + 1)
        #  res = max(res,count)
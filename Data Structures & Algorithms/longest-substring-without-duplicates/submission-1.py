class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res,r-l+1)
        return res
    
# #Approach- charSet = set()
# traverse through s and check if element exist in set - if yes then remove it and increment l else insert it.
# charSet = (p,w,k,e)
# l = 1
# r = 4
# res = 3
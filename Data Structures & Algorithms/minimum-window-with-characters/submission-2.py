class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = defaultdict(int)
        window = defaultdict(int)
        
        for i in t:
            countT[i]+=1
        need = len(countT)
        have = 0
        l = 0
        res = [-1,-1]
        reslen = float("inf")
        for r in range(len(s)):
            c = s[r]

            if c in countT:
                window[c]+=1
                if window[c] == countT[c]:
                    have+=1

            while have == need:
                if (r-l+1) < reslen:
                    res = [l,r]
                    reslen = r-l+1
                if s[l] in countT:
                    window[s[l]] -=1
                    if window[s[l]] < countT[s[l]]:
                        have-=1
                l+=1

        l,r = res
        return s[l:r+1]


# s = "O U Z O D Y X A Z V", t = "XYZ"
#          l
#                      r

# countT{
#     X:1,
#     Y:1,
#     Z:1
# }
# window = {
#     Z:1,
#     Y:1,
#     X:1
# }
# need = 3
# have = 3
# res = [0,6]
# reslen = 6
# l = 2
# r = 8

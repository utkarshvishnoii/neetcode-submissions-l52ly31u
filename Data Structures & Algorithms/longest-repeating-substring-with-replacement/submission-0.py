class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charS = defaultdict(int)
        l = 0
        res= 0

        for r in range(len(s)):
            charS[s[r]]+=1
            if ((r-l+1) - max(charS.values())) <= k:
                res = max(r-l+1,res)
            else:
                charS[s[l]]-=1
                l+=1
        return res

# s = "A AABABB"
# charS{
#     A:3
#     B:2
# }
# l =1
# r = 0->1->2->3->4->5->6
# res = 5
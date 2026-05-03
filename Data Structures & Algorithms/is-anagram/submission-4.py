class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_new =  defaultdict(int)
        t_new = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s_new[s[i]]+=1
            t_new[t[i]]+=1
        
        for k in s_new:
            if s_new[k] != t_new[k]:
                return False

        return True



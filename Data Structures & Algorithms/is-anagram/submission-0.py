class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs = defaultdict(int)
        hasht = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in s:
            hashs[i] += 1
        for j in t:
            hasht[j] += 1
        
        for i in hashs:
            if hashs[i] != hasht[i]:
                return False
        return True
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram  =defaultdict(list)
        for s in strs:
            key = [0]*26
            for c in s:
                key[ord(c)-ord('a')]+=1
            anagram[tuple(key)].append(s)
        return [i for i in anagram.values()]
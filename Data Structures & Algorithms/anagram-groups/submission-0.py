class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupN = defaultdict(list)
        for word in strs:
            new = ''.join(sorted(word))
            groupN[new].append(word)
        
        return list(groupN.values())

        nlogn * n



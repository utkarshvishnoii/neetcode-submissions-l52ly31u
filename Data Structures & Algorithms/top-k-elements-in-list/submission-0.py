class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countN = defaultdict(int)
        res = []
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            countN[i]+=1
        
        for index,val in countN.items():
            freq[val].append(index)
        count = 0
        for i in freq[::-1]:
            for char in i:
                if count <k:
                    res.append(char)
                    count+=1
        return res

# first create freq list = [[] for i in len(nums)-1]
# second I will create hashmap to maintain count
# insert the value in freq list based on val-counts index
# traverse opp in the list and save k-elemens in new list
# [1,2,2,3,3,3]
# countN = {1:1,2:2,3:3}

# [[],[1],[2],[3]]
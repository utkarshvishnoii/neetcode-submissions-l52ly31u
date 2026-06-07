class Solution:
    def reorganizeString(self, s: str) -> str:
        countS = Counter(s)

        maxHeap = [[-v,k] for k,v in countS.items()]
        heapq.heapify(maxHeap)
        prev = None
        s_new = ""
        while maxHeap or prev:
            if not maxHeap:
                if prev[0] == 0:
                    return s_new
                else:
                    return ""
            cnt,ele = heapq.heappop(maxHeap)

            s_new += ele
            cnt +=1

            if prev is None:
                prev = [cnt,ele]
            else:
                if prev[0] != 0:
                    heapq.heappush(maxHeap,prev)
                prev = [cnt,ele]

                    



# take element from maxHeap and save it in new string
# push the prev back to maxHeap and make the prev None if count is != 0
# store curr element in prev with a decrement of count if prev is None otherwise push it back to heap
# a:2,b:1
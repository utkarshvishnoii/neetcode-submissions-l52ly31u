class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res= []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res+intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                s = intervals[i][0]
                e = intervals[i][1]
                res.append([s,e])
            else:
                newInterval[0] = min(newInterval[0],intervals[i][0])
                newInterval[1] = max(newInterval[1],intervals[i][1])
        res.append(newInterval)
        return res




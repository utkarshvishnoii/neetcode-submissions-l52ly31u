class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        new_interval = []
        new_interval.append(intervals[0])

        for r in intervals:
            start_new = new_interval[-1][0] 
            end_new = new_interval[-1][1]
            start = r[0]
            end = r[1]

            if start <= end_new :
                new_interval[-1][1] = max(end,end_new)
            else:
                new_interval.append([start,end])
        return new_interval


# new_interval = [[1,3]]
# r = [2,3]
# start_new =1
# end_new=2
# start = 2
# end = 3
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_list = []
        for point in points:
            first = point[0]
            second = point[1]
            distance = math.sqrt((first*first) + (second*second))

            dist_list.append([distance,point])
        heapq.heapify(dist_list)
        res = []

        while len(res) < k:
            p = heapq.heappop(dist_list)
            res.append(p[1])
        return res
# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         taskN = Counter(tasks)
#         heap = [(-v,k) for k,v in taskN.items()]
#         heapq.heapify(heap)
#         q = deque()
#         time = 0
#         while heap or q:
#             time+=1
#             if heap:
#                 taskCnt,taskName = heapq.heappop(heap)
#                 taskCnt +=1
#             if taskCnt != 0:
#                 q.append(((taskCnt,taskName),time+n))

#             if q and q[0][1] == time:
#                 heapq.heappush(heap,q.popleft()[0])
#         return time


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskN = Counter(tasks)

        heap = [-v for v in taskN.values()]
        heapq.heapify(heap)

        q = deque()   # [count, available_time]
        time = 0

        while heap or q:
            time += 1

            if heap:
                cnt = 1 + heapq.heappop(heap)

                if cnt != 0:
                    q.append((cnt, time + n))

            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])

        return time

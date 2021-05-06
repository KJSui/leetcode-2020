import heapq
class Solution:
    def leastInterval(self, tasks, n):
        mp = {}
        for i in tasks:
            if i not in mp:
                mp[i] = 1
            else:
                mp[i] += 1
        queue = []
        for i in mp.keys():
            heapq.heappush(queue, [-mp[i], i])

        time = 0

        while len(queue) > 0:
            tmp = []
            start = 0
            while start <= n:
                if len(queue):
                    if -queue[0][0] > 1:
                        r = heapq.heappop(queue)
                        r[0] += 1
                        tmp.append(r)

                    else:
                        heapq.heappop(queue)
                start += 1
                time += 1

                if len(queue) == 0 and len(tmp) == 0:
                    break 
            for q in tmp:
                heapq.heappush(queue, q)

        return time 
            

obj = Solution()
tasks = ["A","A","A","B","B","B"]
n = 2
print(obj.leastInterval(tasks, n))

while len(queue) > 0:
    tmp = []
    start = 0
    while start < n:
        if len(queue) > 0:
            slot = heapq.heappop(queue)
            if slot[-1] > 1:
                slot[-1] += 1
                tmp.append(slot)
            start += 1
            res += 1

        if len(queue) == 0 and len(tmp) == 0:
            break
        for q in tmp:
            heapq.heappush(queue, q)
    
class Solution:
    def leastInterval(self, tasks, n):
        mp = {}
        hp = []

        for i in tasks:
            if i not in mp:
                mp[i] = 1
            else:
                mp[i] += 1

        for i in mp.keys():
            pair = [-mp[i], i]
            heapq.heappush(hp, pair)

        time = 0
        while len(hp):
            tmp = []
            while len(hp):
                k = heapq.heappop(hp)
                if k[0] < -1:
                    k[0] += 1
                    tmp.append(k)
                time += 1
                if not len(hp) and not len(tmp):
                    break
                i += 1

            for m in tmp:
                heapq.heappush(hp, m)
        return time

        

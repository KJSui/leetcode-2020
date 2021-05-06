import heapq
class Solution:
    def meetingRoom2(self, intervals):
        free_room = []
        intervals.sort(key = lambda x: x[0])
        heapq.heappush(free_room, [intervals[0][1], intervals[0][0]])
        room_num = 0
        res = {}

        for i in intervals[1:]:
            if i[0] >= free_room[0][0]:
                heapq.heappop(free_room)
            heapq.heappush(free_room, [i[1], i[0]])

        rooms_len = len(free_room)
        while room_num < rooms_len:
            v = heapq.heappop(free_room)
            res[room_num] = [v[1], v[0]]
            room_num += 1
        #initilize
        final = {}
        for i in res:
            final[i] = [[res[i][0], res[i][1]]]
        #compare and classify
        for i in intervals:
            for j in res.keys():
                if i[0] >= res[j][1] or i[1] <= res[j][0]:
                    res[j][1] = max(res[j][1], i[0])
                    res[j][0] = min(res[j][0], i[1])
                    final[j].append(i)
                    break

intervals = [[0, 30], [5, 10], [15, 20], [21, 29], [11, 16]]
obj = Solution()
print(obj.meetingRoom2(intervals))
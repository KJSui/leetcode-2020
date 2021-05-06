import heapq
class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            print("maxGap:", 0)
            return 0

        gap = 0
        intervals.sort(key = lambda x: x[0])

        rooms = []
        heapq.heappush(rooms, intervals[0][1])

        for i in intervals[1:]:
            if rooms[0] <= i[0]:
                heapq.heappop(rooms)
            else:
                gap = max(gap, min(rooms[0] - i[0], i[1]-i[0]))
            heapq.heappush(rooms, i[1])
        print("maxGap: ", gap)
        return len(rooms)

obj = Solution()
intervals = [[0, 30], [5, 10], [15, 20]]
print(obj.minMeetingRooms(intervals))
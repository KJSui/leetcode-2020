class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x: x[0])
        i = 1
        free_room = []
        while i < len(intervals):
            if intervals[i][0] > intervals[i-1][1]:
                free_room.append([intervals[i-1][1], intervals[i][0]])
            else:
                intervals[i][1] = max(intervals[i][1], intervals[i-1][1])
            i += 1

        return free_room
    

                
                
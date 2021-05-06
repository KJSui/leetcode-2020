class Solution:
    def mergeSortedListIntervals(self, list1, list2):
        interval1 = self.mergeIntervals(list1)
        interval2 = self.mergeIntervals(list2)
        for k in interval1:
            left = 0
            right = len(interval2)-1
            while left < right:
                mid = left + (right-left)//2
                if intervals2[mid][0] < k[0]:
                    left = mid + 1
                else:
                    right = mid
            if k[0] > interval2[left][0]:
                if k[0] > interval2[left][1]:
                    interval2 = interval2[:left+1] + k + interval2[left+1:]
                else:
                    interval2[1] = max(interval2[1], k[1])
            else:
                if k[1] >= interval2[0]:
                    interval2[0] = k[0]
                    interval2[1] = max(interval2[1], k[1])
        return interval2

    def mergeIntervals(self, intervals):
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals
        #intervals.sort(key=lambda x: x[0])
        j = intervals[0]
        i = 1
        while i < len(intervals):
            tmp = intervals[i]
            if intervals[i][0] <= j[1]:
                intervals[i][0] = j[0]
                intervals[i][1] = max(j[1],intervals[i][1])
                intervals.pop(i-1)
            else:
                i += 1
            j = tmp

        return intervals

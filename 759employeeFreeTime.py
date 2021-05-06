class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
class Solution:
    def employeeFreeTime(self, schedule):
        event = []
        OPEN, CLOSE = 0, 1
        for i in schedule:
            for j in i:
                event.append([j.start, OPEN])
                event.append([j.end, CLOSE])
                
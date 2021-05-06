class Solution:
    def countOfAirlines(self, airplanes):
        if len(airplanes) == 0:
            return 0
        start = []
        end = []
        for i in airplanes:
            start.append(i[0])
            end.append(i[1])

        sorted(start)
        sorted(end)

        startidx = 0
        endidx = 0
        curr = 0
        maxv = 0

        while startidx < len(airplanes):
            if start[startidx] < end[endidx]:
                startidx += 1
                curr += 1

            else:
                curr -= 1
                endidx += 1

            maxv = max(maxv, curr)

        return maxv
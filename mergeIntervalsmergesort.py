class Solution:

    def __init__(self):
        self.res = []

    def mergeSortIntervals(self, array):
        if len(array) > 1:
            mid = len(array)//2
            left = array[:mid]
            right = array[mid:]
            self.mergeSortIntervals(left)
            self.mergeSortIntervals(right)
            i = j = k = 0

            while i < len(left) and j < len(right):
                array[k] = self.mergeInterval(left[i], right[j])
                k += 1
                i += 1
                j += 1

        return array[0]

    def mergeInterval(self, interval1, interval2):
        array = interval1[:] + interval2[:]
        sorted(array)
        i = 0
        j = 1
        while j < len(array):
            if array[i][1] >= array[j][0]:
                array[i][0] = min(array[i][0], array[j][0])
                array[i][1] = max(array[i][1], array[j][1])
                array = array[:j]+array[j+1:]

            else:
                j += 1
                i += 1
        return array

obj = Solution()
array = [
[[13.5, 14], [15.75, 17]],
[[9, 12], [13, 14], [14, 16]],
[[9, 11], [12.5, 13.5], [14, 15], [16, 18]],
[[0, 9], [12, 24]]
]
print(obj.mergeSortIntervals(array))

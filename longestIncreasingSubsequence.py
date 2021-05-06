class Solution：
    def longestIncreasingNumber(self, num):
        top = 0
        b = [float('-inf')]*len(num)
        for i in range(len(num)):
            start = 0
            stop = top
            mid = 0
            j = -1

            while start <= stop:
                mid = start + (stop - start)//2
                if b[mid] < num[i]:
                    j = mid
                    start = mid + 1
                else:
                    stop = mid - 1

            b[j+1] = num[i]
            if j + 1 > top:
                top = j + 1

        return top
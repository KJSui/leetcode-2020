class Solution:
    def findLeftmostOne(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        start_row = 0
        start_col = col-1
        res = col
        while start_row < row and start_col >= 0:
            while start_row < row and (matrix[start_row][start_col] == 0):
                start_row += 1
            if start_row == row:
                break
            start_col = self.binarysearch(matrix[start_row])
            res = min(res, start_col)
            start_row += 1
        if res < col:
            return res
        return -1

    def binarysearch(self, array):
        left = 0
        right = len(array)-1
        while left < right:
            mid = left + (right-left)/2
            if array[mid] == 1:
                right = mid
            else:
                left = mid+1
        return left

obj = Solution()
matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],[0, 0, 0, 0]]
print(obj.findLeftmostOne(matrix))

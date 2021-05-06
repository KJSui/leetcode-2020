
class Solution:
    def kthSmallestElement(self, matrix, k):
        row_l = len(matrix)-1
        col_l = len(matrix[0])-1
        min_v = matrix[0][0]
        max_v = matrix[row_l][col_l]

        while min_v < max_v:
            mid = min_v + int((max_v-min_v)/2)
            if self.possible(matrix, k, mid) >= k:
                max_v = mid 
            else:
                min_v = mid + 1

        return min_v 

    def possible(self, matrix, k, mid):
        i = len(matrix)-1
        j = 0
        count = 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] <= mid:
                count += i+1
                j += 1
            else:
                i -= 1

        return count 
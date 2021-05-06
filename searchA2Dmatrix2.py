class Solution:
    def search2Dmatrix2(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row_mid = self.binary(matrix[0], target)
        print("row_mid: ", row_mid)

        if matrix[0][row_mid] == target:
            return True
        col_mid = 0
        for j in range(len(matrix)):
            if matrix[j][row_mid] == target:
                return True
            elif matrix[j][row_mid] > target:
                col_mid = j
                break
        print("col_mid: ", col_mid)
        
        row_mid = self.binary(matrix[col_mid][:row_mid], target)
        if matrix[col_mid][row_mid] == target:
            return True
        
        row_mid = self.binary(matrix[col_mid-1][row_mid:], target)
        if matrix[col_mid][row_mid] == target:
            return True
            
        return False
        
    def binary(self, array, target):
        l = 0
        r = len(array)-1
        while l <= r:
            mid = l + (r-l)//2
            if array[mid] < target:
                l = mid+1
            elif array[mid] == target:
                return mid
            else:
                r = mid-1
                
        if l >= len(array) or array[l] > target:
            return r 
        return l

obj = Solution()
matrix = [[2,5],[2,8],[7,9],[7,11],[9,11]]
target = 7
print(obj.search2Dmatrix2(matrix, target))
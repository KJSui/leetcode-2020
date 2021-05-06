class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)-1
        n = len(matrix[0])-1
        mid  = matrix[0][0]
        minv = matrix[0][0]
        maxv = matrix[m][n]
        cnt = 0
        while minv < maxv:
            mid = minv + int((maxv-minv)/2)
            print("minv:", minv, "maxv:", maxv, "mid:", mid)
            cnt = self.possible(matrix, k, mid)
            print("cnt:", cnt, "k:", k)
            if cnt >= k:
                maxv = mid
            elif cnt < k:
                minv = mid+1  
                
        return minv
    
    def possible(self, matrix, k, mid):
        i = len(matrix)-1
        j = 0
        cn = 0
        while(i >= 0 and j < len(matrix)):
            if matrix[i][j] <= mid:
                cn += i+1
                j += 1
            else:
                i -= 1
        return cn
            
                
matrix = [[1, 2], [1, 3]]
obj = Solution()
print(obj.kthSmallest(matrix, 3))
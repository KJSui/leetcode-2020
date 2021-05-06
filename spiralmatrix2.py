class Solution:
    def spiralMatrix2(self, n):
        A = [[0]*n for i in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            A[i][j] = k+1
            if A[(i+di)%n][(j+dj)%n]:
                i, j = dj, -di   

            i += di      
            j += dj 

        return A   
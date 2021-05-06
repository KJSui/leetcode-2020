class Solution:
    def backpack(self, A, m):
        f  =[[False]*(m+1) for i in range(2)]
        f[0][0] = True 
        for i in range(len(A)):
            for j in range(m+1):
                f[(i+1)%2][j] = f[i%2][j]
                if ( j >= A[i]) && f[i%2][j-A[i]]:
                    f[(i+1)%2][j] = True 


        for i in range(m, -1, -1):
            if f[len(A)%2][i]:
                return i  

        return 0
                    


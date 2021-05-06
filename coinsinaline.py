class Solution:
    def firstWillWin(self, A):
        n = len(A)
        if not n:
            return True

        f = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            f[i][i] = A[i]

        for l in range(2, n+1):
            for j in range(n-l+1):
                k = j + l - 1
                f[j][k] = max(A[j] - f[j+1][k], A[k] - f[j][k-1])

        return f[0][n-1] >= 0

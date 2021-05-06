class Solution:
    def backpack2(self, A, V, m):
        f[i][w] = max(f[i-1][w], f[i-1][w-A[i-1]] + V[i-1])

        f = [[0] * (len(A)+1) for _ in range(m+1)]

        for i in range(1, len(A)):
            j = m
            while j - A[i] >= 0:
                f[i][j] = max(f[i-1][j], f[i-1][j-A[i-1]] + V[i-1])

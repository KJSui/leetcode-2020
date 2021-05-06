class Solution:
    def minFallingPathSum(self, A):
        N = len(A)
        for r in range(N-2, -1， -1):
            for j in range(0, N):
                best = A[r+1][j]
                if j > 0:
                    best = max(A[r+1][j-1], best)
                if j+1 < N:
                    best = max(A[r+1][j+1], best)
                A[r][j] += best

        return min(A[0])

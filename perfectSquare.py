class Solution:
    def numSquares(self, n):
        dp = [n] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            m = n
            j = 1
            while i - j*j >= 0:
                m = min(m, dp[i-j*j]+1)
                j += 1

            dp[i] = m
        return dp[n]
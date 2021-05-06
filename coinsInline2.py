class Solution:   
    def coinsInLine2(self, A):
        res = 0
        self.dp = [0]*(len(A)+1)
        if len(A) <= 2:
            return True 
        self.dp[n-1] = A[n-1]
        self.dp[n-2] = A[n-2] + A[n-1]
        self.dp[n-3] = A[n-3] + A[n-2]

        for i in range(n-4, -1, -1):
            self.dp[i] = max(A[i]+min(self.dp[i+2], self.dp[i+3]), A[i]+A[i+1]+min(self.dp[i+3], self.dp[i+4]))
        for d in A:
            res += d
        return res - dp[0] < dp[0]
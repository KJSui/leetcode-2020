class Solution:
    def longestArithSeqLength(self, A):
        if len(A) == 2:
            return 2
        minv = min(A)
        maxv = max(A)
        maxDiff = maxv - minv
        res = 0
        dp = [[0] *(2*maxDiff + 1)] * len(A)
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j] + maxDiff
                dp[i][diff] = max(dp[i][diff], dp[j][diff]+1)
                res = max(res, dp[i][diff])

        return res + 1

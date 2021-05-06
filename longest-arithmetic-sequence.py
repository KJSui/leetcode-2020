class Solution:

    def longest-arithmetic-sequence(self, A):
        if len(A) == 0:
            return 0
        max_v = A[0]
        min_v = A[0]
        for i in A:
            if i > max_v:
                max_v = i 
            if i < min_v:
                min_v = i
        max_diff = max_v - min_v 
        dp = [0 *(2 * max_diff+1)] * len(A)
        ans = 0
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j] + max_diff
                dp[i][diff] = max(dp[i][diff], dp[j][diff]+1)
                if ans < dp[i][diff]:
                    ans = dp[i][diff]

        return ans+1

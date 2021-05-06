class Solution:
    def findmaxcoins(self, arrays):
        row = len(arrays)
        col = len(arrays[0])

        dp = [[0 for i in range(col)] for j in range(len(row))]


        for i in range(1, row):
            for j in range(1, col):
                for k in range(col):
                    dp[i][j] = max(dp[i][j], dp[i-1][k]-abs(j-k))
                    

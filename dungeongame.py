class Solution:
    def dungeongame(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[float('inf')]*(n+1) for _ in range(m+1)]
        dp[m][n-1] = 1
        dp[m-1][n] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                need = min(dp[i][j+1], dp[i+1][j]) - dp[i][j]
                if need <= 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = need


        return dp[0][0] 
class Solution:
    def stoneGame2(self, piles):
        dp = [[-1 for _ in range(len(piles)+1)] for _ in range(len(piles)+1)]
        sums = [0] * len(piles)
        sums[-1] = piles[-1]

        for i in range(len(piles)-2, -1, -1):
            sums[i] = piles[i] + sums[i+1]

        for i in range(len(piles)+1):
            dp[-1][i] = 0

        return self.recur(1, 0)
        
    def recur(self, m, j):
        if dp[m][j] != -1:
            return dp[m][j]

        result = 0
        for i in range(1, min(2*m, len(piles)-j)+1):
            result = max(result, sums[j] - self.recur(max(i, m), j + i))
        dp[m][j] = result

        return result

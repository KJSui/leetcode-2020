class Solution:
    def stoneGames(self, piles):
        N = len(piles)

        res = [[0 for i in range(0, N+2)] for j in range(0, N+2)]

        for i in range(1, N+1):
            for j in range(N, i-1, -1):
                #j = i + size - 1
                parity = (i + j + N)%2
                if parity == 1:
                    res[i][j] = max(piles[i-1] + res[i+1][j], piles[j-1] + res[i][j-1])
                else:
                    res[i][j] = max(-piles[i-1] + res[i+1][j], -piles[j-1] + res[i][j-1])
        return res[1][N] > 0



obj = Solution()
piles = [1, 3, 4, 5, 1]
print(obj.stoneGames(piles))
class Solution:
    def checkreachingend(self, array):
        dp = [False for j in range(len(array))]
        for i in range(0, len(array)):
            for j in range(0, len(array[0])):
                if array[i][j]:
                    dp[j] = False
                    continue
                if i == 0 and j == 0:
                    dp[j] = True
                    continue
                if i == 0 and dp[(j-1)]:
                    dp[j] = True
                    continue
                if j == 0 and dp[(i-1)%2][j%2]:
                    dp[i%2][j%2] = True
                    continue
                dp[i%2][j%2] = True if (dp[i%2][(j-1)%2] or dp[(i-1)%2][j%2]) else False

        return dp[(len(array[0]))-1]

obj = Solution()
array = [
  [0,1,0],
  [0,0,0],
  [0,1,0],
]
print(obj.checkreachingend(array))

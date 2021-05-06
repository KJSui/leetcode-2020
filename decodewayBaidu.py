class Solution:
    def decodeWay(self, s):
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s)+1):
            if (s[i-2] == '1') or (s[i-2] == '2' and s[i-1] < '7'):
                if s[i-1] != '0':
                    dp[i] = dp[i-2] + dp[i-1]
                else:
                    dp[i] = dp[i-2]
            else:
                if s[i-1] != '0':
                    dp[i] = dp[i-1]
        return dp[len(s)]

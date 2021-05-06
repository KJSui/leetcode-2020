class Solution:
    def numDecodings(self, s):
        M = 1000000007
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        if s[0] == "*":
            #print("here")
            dp[1] = 9
        elif s[0] == '0':
            dp[1] = 0
        else:
            dp[1] = 1
            
        for i in range(2, len(s)+1):
            if s[i-1] == "*":
                dp[i] = 9 * dp[i-1]
                if s[i-2] == '1':
                    dp[i] = (dp[i] + 9 * dp[i-2])%M
                elif s[i-2] == '2':
                    dp[i] = (dp[i] + 6*dp[i-2])%M
                elif s[i-2] == '*':
                    dp[i] = (dp[i] + 15 * dp[i-2])%M
            else:
                if s[i-1] == '0':
                    dp[i] = 0
                else:
                    dp[i] = dp[i-1]
                    
                if s[i-2] == '1':
                    dp[i] = (dp[i] + dp[i-2]) %M
                elif s[i-2] == '2' and s[i-1] <= '6':
                    dp[i] = (dp[i] + dp[i-2])%M
                elif s[i-2] == '*':
                    if s[i-1] <= '6':
                        dp[i] = (dp[i] + 2 * dp[i-2])%M
                    else:
                        dp[i] = (dp[i] + dp[i-2])%M
        print("dp array:", dp)   
        return dp[n]

obj = Solution()
s = "2839"
print(obj.numDecodings(s))
class Solution:
    def palindromePartiton2(self, s):
        n = len(s)
        f = [0]*(n+1)
        for i in range(n+1):
            f[i] = n-1-i  
        p = [[False for i in range(n)] for j in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and ((j - i < 2) or p[i+1][j-1]):
                    p[i][j] = True 
                    f[i] = min(f[j+1]+1, f[i])
        

        return f[0]

s = "aabc"
obj = Solution()
print(obj.palindromePartiton2(s))

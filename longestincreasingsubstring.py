class Solution:
    def longestIncreasingSubstring(self, num):
        f = [0]*(len(num))
        f[0] = 1
        ans = 1
        res = 0
        for i in range(1, len(num)):
            for j in range(i):
                if num[i] > num[j]:
                    res = max(res, f[j])
            f[i] = res + 1
            ans = max(ans, f[i])

        return ans


        
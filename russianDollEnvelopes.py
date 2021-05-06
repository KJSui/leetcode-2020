from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, arr):
        arr.sort(key=lambda x: (x[0], -x[1]))

        def lis(num):
            dp = []
            for i in range(len(num)):
                idx = bisect_left(dp, num[i])
                if idx == len(dp):
                    dp.append(num[idx])
                else:
                    dp[idx] = num[i]

            return len(dp)

        return lis([i[1] for i in arr])


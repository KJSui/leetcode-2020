class Solution:
    def countSubstrings(self, s):
        N = len(s)
        res = 0
        for i in range(2 * N):
            left = int(i/2)
            right = left + i%2
            while left >= 0 and right < N and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

        return res

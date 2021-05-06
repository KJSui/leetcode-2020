class Solution:
    def countSubstrings(self, s):
        N = len(s)
        res = 0
        for c in range(2*N):
            left = int(c/2)
            right = left + c%2
            while left >= 0 and right < N and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

        return res 
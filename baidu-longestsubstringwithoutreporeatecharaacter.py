class Solution:
    def longestSubstringWithoutRepeatedCha(self, s):
        mp = {}
        start = 0
        res = 0
        for i in range(len(s)):
            if s[i] in mp.keys():
                start = mp[s[i]] + 1
            else:
                res = max(res, i - start + 1)
            mp[s[i]] = i

        return res

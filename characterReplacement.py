class Solution:
    def characterReplacement(self, s, k):
        N = len(s)
        if N <= 1:
            return N

        char2idx = {chr(ord('A')+i): i for i in range(26)}
        cnts = [0]*26
        valid = 1
        begin = 0
        end = 1
        res = 1
        cnts[char2idx[s[0]]] = 1
        while end < len(s):
            if valid:
                cnts[char2idx[end]] += 1
                end += 1
            else:
                cnts[char2idx[begin]] -= 1
                begin += 1

            valid = (end-begin-max(cnts) <= k)
            if valid:
                res = max(res, end-start)
        return res

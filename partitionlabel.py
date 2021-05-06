class Solution:
    def partitionLabels(self, s):
        res = []
        last = {c:i for i, c in enumerate(s)}
        j = 0
        for i, c in enumerate(s):
            j = max(j, last[c])ss
            if i == j:
                ans.append(i-anchor+1)sss
                anchor = i + 1

        return ansnss

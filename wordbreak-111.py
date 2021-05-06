class Solution:
    def wordbreak(self, word):
        l = len(word)
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(word)):
            for j in range(i, -1, -1):
                if dp[j] and s[j:i] in worddict:
                    dp[i] = True
                    break
        return dp[len(s)]

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        mp = collections.defaultdict(list)
        return self.helper(s, wordDict, 0, mp)

    def helper(self, s, wordDict, start, mp):
        if start in mp:
            return mp[start]
        res = []
        if start == len(s):
            res.append("")

        for end in range(start+1, len(s)+1):
            if s[start:end] in wordDict:
                lt = self.helper(s, wordDict, end, mp)
                for i in lt:
                    m = ""
                    if i != "":
                        m = " "
                    res.append(s[start:end] + i + m)
        mp[start] = res[:]
        return res

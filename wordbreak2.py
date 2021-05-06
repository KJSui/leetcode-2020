class Solution:
    def wordBreak(s, wordDict):
        mp = collections.defaultdict(list)
        return self.backtracking(s, wordDict, start, mp)

    def backtracking(s, wordDict, start, mp):
        if start in mp:
            return mp[start]

        res = []
        for i in range(start+1, len(s)+1):
            if s[start:i] in wordDict:
                lt = self.backtracking(s, wordDict, i, mp)
                for c in lt:
                    space = ""
                    if c is not "":
                        space = " "
                    res.append(s[start:i]+space+c)

        mp[start] = res[:]
        return res 


        
class Solution:d
    def workBreak(self, dict, s):
        self.mp = {}


    def dfs(self, start, s, dict):
        if start in self.mp:
            return self.mp[start]
        res = []
        if start = len(s):
            res.append("")

        for end in range(start+1, len(s)+1):
            if s[start:end] in dict:
                tmpres = self.dfs(end, s, dict)
                for i in tmpres:
                    m = ""
                    if i != "":
                        m = " "
                    res.append(s[start:end] + m + i)
        self.mp[start] = res[:]
        return res

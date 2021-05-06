    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        par = ["(", ")"]
        self.ans = []
        self.helper(s, ans, 0, 0, par)
        return ans
    def helper(self, s, ans, i, lastj, par):
        count = 0
        for i in range(len(s)):
            if s[i] == par[0]:
                count += 1
            if s[i] == par[1]:
                count -= 1
            if count >= 0:
                continue
            j = lastj
            while j <= i:
                if s[j] == ")" and (s[j] == lastj or s[j-1] != "("):
                    self.helper(s[:j]+s[j+1:], ans, i, j, par)

                j += 1

            return 
        reversed = s[::-1]
        if par[0] == "(":
            self.helper(reversed, ans, 0, 0, [")", "("])
        else:
            self.ans.append(reversed)
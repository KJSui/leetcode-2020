class Solution:
    def addOperators(self, num, target):
        self.res = []
        self.dfs(0, 0, 0, 0, [])
        return self.res
    def dfs(self, num, target, idx, prev, curr, value, string):
        if idx == len(num):
            if value == target and curr == 0:
                self.res.append("".join(string[1:]))
            return

        curr = curr * 10 + int(num[idx])
        str_op = str(curr)
        if curr > 0:
            self.dfs(num, target, idx+1, prev, curr, value, string)
        string.append('+')
        string.append(str_op)
        self.dfs(num, target, idx+1, prev, 0, value+curr, string)
        string.pop()
        string.pop()

        if string:
            string.append('-')
            string.append(str_op)
            self.dfs(idx+1, -curr, 0, value-curr, string)
            string.pop()
            string.pop()

            string.append('*')
            string.append(str_op)
            self.dfs(idx+1, curr * prev, 0, value-prev+ curr * prev, string)
            string.pop()
            string.pop()

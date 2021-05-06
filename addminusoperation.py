class Solution:
    def getAllPathTarget(self, num, target):
        self.res = []
        idx = 0
        curr_sum = 0
        self.dfs(num, target, idx, curr_sum, [], 0)
        return self.res

    def dfs(self, num, target, idx, curr_sum, string, curr_op):
        if idx == len(num):
            if curr_sum == target and not curr_op:
                self.res.append("".join(string[1:]))
            return

        curr_op = curr_op*10 + num[idx]
        str_op = str(curr_op)

        if curr_op > 0:
            self.dfs(num, target, idx+1, curr_sum, string, curr_op)

        #add
        string.append('+')
        string.append(str_op)
        self.dfs(num, target, idx+1, curr_sum + curr_op, string,  0)
        string.pop()
        string.pop()


        #minus:
        if string:
            string.append('-')
            string.append(str_op)
            self.dfs(num, target, idx+1, curr_sum - curr_op, string, 0)
            string.pop()
            string.pop()

        return

obj = Solution()
num = [1, 0, 5]
target = 6
print(obj.getAllPathTarget(num, target))

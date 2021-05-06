class Solution:
    def candaCrash(self, string):
        stack = []
        start = 0
        while start < len(string):
            if len(stack) == 0:
                stack.append([string[start], 1])
            else:
                if string[start] != stack[-1][0]:
                    if stack[-1][1] >= 3:
                        stack.pop()
                        continue
                    stack.append([string[start], 1])
                else:
                    stack[-1][1] += 1
            start += 1

        if len(stack) == 0:
            return ""
        res = ""
        print(stack)
        while len(stack):
            c, cnt = stack.pop()
            if cnt < 3:
                res = c*cnt + res
        return res
obj = Solution()
string = "abbbaac"
print(obj.candaCrash(string))

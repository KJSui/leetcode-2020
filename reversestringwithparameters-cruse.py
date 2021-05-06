class Solution:
    def reverse(self, string):
        stack = []
        res = ""
        start = 0
        left = 0
        queue = []
        while start < len(string):
            if string[start] not in ['(', ')']:
                if left == 0:
                    res += string[start]
                else:
                    stack.append(string[start])
            elif string[start] == '(':
                left += 1
                stack.append(string[start])
            else:
                left -= 1
                while len(stack):
                    top = stack.pop()
                    if top == '(':
                        if len(stack) == 0:
                            res += ''.join(queue)
                        else:
                            stack += queue
                        queue = []
                    else:
                        queue.append(top)
            start += 1
        return res
obj = Solution()
string = "(123)45(67(89))"
print(obj.reverse(string))


                

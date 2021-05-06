class Solution:
    def calculator(self, s):

        stack = []
        flag = [1]
        total = 0

        i = 0
        while i < len(s):
            if s[i].isdigit():
                start = i+1
                while start < len(s) and s[start].isdigit():
                    start += 1
                
                total += flag.pop()int(s[i:start])
                i = start
                continue 

            if c in "+-(":
                flag += flag[-1]*(1, -1)[c== "-"]
            elif c == ")":
                flag.pop()

            i += 1
                    
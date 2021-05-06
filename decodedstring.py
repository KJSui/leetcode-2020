class Solution:
    def decodeString(self, s):
        stack = []
        i = 0
        n = len(s)
        while i < n:
            c = s[i]
            if self.checknum(c):
                j = i
                while self.checknum(c):
                    j += 1
                stack.append(s[i:j])
                i = j

            elif c == '[':
                i += 1
            elif c == ']':
                tmpstring = ''
                while True:
                    tmp = stack.pop()
                    if self.checknum(tmp):
                        stack.append(int(tmp) * tmpstring)
                        tmpstring = ""
                        break
                    tmpstring = tmp + tmpstring
                i += 1
            else:
                stack.append(c)
                i += 1

        while len(stack):
            res = stack.pop() + res

        return res


#dp algorithm

class Solution:
    def decodeString(self, s):
        repeat = 0
        idx = 0
        while idx < len(s):
            ch = s[idx]
            if ch == ']':
                return ''.join(ans)
            elif ch == '[':
                idx += 1
                string = self.decodeString(s[idx:])
                if repeat > 0:
                    ans.append(repeat * string)
            elif ch.isdigit():
                repeat = repeat * 10 + ord(ch) - ord('0')
            else:
                ans.append(ch)
            idx += 1

        return "".join(ans)

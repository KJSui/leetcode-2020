class Solution:
    def decodeString(self, s):
        self.stack = []
        i = 0
        res = ""
        tmpstring = ""

        while i < len(s):
            c = s[i]
            if self.checknum(c):
                while self.checknum(c):
                    tmpstring += c
                    i += 1
                    c = s[i]

                self.stack.append(tmpstring)
                tmpstring = ""

            elif c == '[':
                i += 1
            elif c == ']':
                while True:
                    tmp = self.stack.pop()
                    if self.checknum(tmp[0]):
                        tmpstring =
                         tmpstring * int(tmp)
                        self.stack.append(tmpstring)
                        tmpstring = ""
                        break
                    else:
                        tmpstring = tmp + tmpstring
                    i += 1

            else:
                self.stack.append(c)
                i += 1

        while len(self.stack):
            res = self.stack.pop() + res

        return res

    def checknum(self, c):
        if ord(c) >= ord('0') and ord(c) <= ord('9'):
            return True
        return False

obj = Solution()
s = "3[a]2[bc]"
print(obj.dec)

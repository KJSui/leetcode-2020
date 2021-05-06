class Solution:
    def isNumber(self, s):
        s = s.strip()
        pointSeen = False
        numberSeen = False
        numberAfterE = True
        eSeen = False
        for i in range(len(s)):
            if s[i] >= '0' and s[i] <= '9':
                numberSeen = True
                numberAfterE = True
            elif s[i] == '.':
                if eSeen  or pointSeen:
                    return False
                pointSeen = True
            elif s[i] == 'e':
                if not numberSeen or eSeen:
                    return False
                numberAfterE = False
                eSeen = True

            elif s[i] == '+' or s[i] == '-':
                if i!= 0 and s[i-1] != 'e':
                    return False
            else:
                return False
            return numberSeen and numberAfterE

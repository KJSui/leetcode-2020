class Solution:
    def decodeWays(self, s):
        res = [0]*(len(s)+1)
        res[0] = 1
        res[1] = 1

        for i in range(len(s)+1):
            if s[i-2] == "1" or s[i-2] == "2" and s[i-1] < "7":
                if s[i-1] != "0"
                    s[i] = s[i-2] + s[i-1]
                else:
                    s[i] = s[i-2]

            else:
                if s[i-1] != "0":
                    s[i] = s[i-1]

        return s[len(s)]
    


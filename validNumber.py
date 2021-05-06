class Solution:
    def validNumber(self, s):
        #remove beginning  and end space
        s = s.strip()

        numberSee = False
        numberAfterE = False
        eSee = False
        pointSee = False

        for i in range(len(s)):
            if s[i] >= '0' and s[i] <= '9':
                numberAfterE = True 
                numberSee = True 

            elif s[i] == ".":
                if pointSee or eSee:
                    return False 
                pointSee = True

            elif s[i] == "e":
                if eSee or not numberSee:
                    return False 
                eSee = True 
                numberAfterE = False 

            elif s[i] == "+" or s[i] == "-":
                if i != 0 and s[i-1] != "e":
                    return False 
            else:
                return False 

        return numberAfterE and numberSee

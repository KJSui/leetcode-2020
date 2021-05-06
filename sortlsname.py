class Solution:
    def sortLS(self, lt):
        

    def compareTwoString(self, s1, s2):
        i = j = 0
        while i < len(s1) and j < len(s2):
            if self.checkDigit(s1[i]) and self.checkDigit(s2[j]):
                if int(s1[i]) < int(s2[j]):
                    return -1
                elif int(s1[i]) == int(s2[j]):
                    i += 1
                    j += 1
                else:
                    return 1
        if i < len(s1):
            return 1
        if j < len(s2):
            return -1
        


    def checkDigit(self, char):
        if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return True 
        return False 
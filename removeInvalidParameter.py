class Solution:
    def removeInvalidPaarameter(self, s):


    def helper(self, s, left, right, index, removeNum, newS):
        if index == len(s):
            if left == right:
                if removeNum < self.min:
                    self.min = removeNum
                    res = ''.join(newS)
                elif removeNum == self.min:
                    res = ''.join(newS)

        else:
            if s[index] != '(' and s[index] != ')':
                self.helper(s, left, right, index+1, removeNum, newS+[s[index]])


            else:

                self.helper(s, left, right, index+1, removeNum+1, newS)
                if s[index] == '(':
                    self.helper(s, left+1, right, index+1, removeNum, newS+[s[index]])

                elif right < left:
                    self.helper(s, left, right+1, index+1, removeNum, newS+[s[index]])
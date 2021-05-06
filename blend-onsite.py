class Solution:
    def getRoundedNumber(self, num):
         return [int(num), int(num)+1]
    
    def findBestAnswer(self, array):
        roundedArray = []
        for i in array:
            roundedArray.append(self.getRoundedNumber(i))
        self.array = array[:]
        self.minv = sum(num)
        self.res = []
        self.helper([], roundedArray)
        return self.res

    def getminv(self, combination, array):
        return abs(sum(combination) - sum(array))
    def helper(self, combination, target, array):
        if len(array) == 0:
            if sum(combination) == target:
                v = self.getminv(combination, self.array)
                if self.minv > v:
                    self.minv = v
                    self.res = combination[:]
            return

        for i in array[0]:
            self.helper(combination + [i], target, array[1:])
        
        return 
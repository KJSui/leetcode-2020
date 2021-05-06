class Solution:
    def __init__(self):
        #arraylist
        self.res = []
        
    def booking(self, interval):
        if len(self.res) == 0:
            self.res = [interval]
            return True
        if len(self.res) == 1:
            #print(interval[1], self.res[0][0])
            if interval[1] <= self.res[0][0]:
                
                self.res = [interval] + self.res
                return True
            elif interval[0] >= self.res[0][1]:
                self.res.append(interval)
                return True
            else:
                return False

        index = self.binarySearch(interval[0])
        #print("21--index:", index)
        if index < 0:
            if self.res[0][0] < interval[1]:
                return False
            self.res = [interval] + self.res
            return True

        if self.res[index][1] > interval[0]:
            return False

        if index == len(self.res)-1:
            self.res.append(interval)
            return True
        
        self.res = self.res[:index+1] + [interval] + self.res[index+1:]
        return True

    def binarySearch(self, target):
        start = 0
        end = len(self.res)-1
        while start < end:
            mid = int((start + end)/2)
            if self.res[mid][0] >= target:
                end = mid
            elif self.res[mid][0] < target:
                start = mid + 1
        
        if start >= len(self.res):
            return len(self.res)-1
        else:
            if self.res[start][0] >= target:
                return start-1
            else:
                return start
            
obj = Solution()
test   = [[1, 2], [2, 4], [5, 8], [3, 6]]
for i in test:
    print(obj.booking(i))
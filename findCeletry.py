class Solution:
    def findCeletry(n):
        x = 0
        for i in range(n):
            if know(x, i):
                x = i  
        if any(know(x, i) for i in range(x)):
            return -1 
        if any(not know(i, x) for i in range(x)):
            return -1 
        return x 
                    
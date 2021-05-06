class Solution:
    def nextClosestTime(self, time):
        array = time.split(":")
        digitlist = []
        for i in array:
            for j in i:
                digitlist.append(int(j))
        
        digitlist = sorted(digitlist)
        print("liist: ", digitlist)
        k = len(time)-1
        while k >= 0:
            if time[k] == ":":
                k -= 1
                continue
            
            index = self.findIndex(digitlist, time, k)
            print("index: ", index)
            if index < 0:
                k -= 1
                continue
            
            return time[:k] + str(digitlist[index]) + time[k+1:]
        
        return str(digitlist[0])+str(digitlist[0])+":"+str(digitlist[0])+str(digitlist[0])
    
    def findIndex(self, digitlist, time, k):
        base = int(time[k])
        print("base value: ", base)
        if k == 0:
            for i in range(len(digitlist)):
                if digitlist[i] > base and digitlist[i] <= 2:
                    return i
                if digitlist[i] > 2:
                    return -1
            return -1
        if k == 1:
            if time[0] == "0":
                for i in range(len(digitlist)):
                    if digitlist[i] > base:
                        return i
            else:
                for i in range(len(digitlist)):
                    if digitlist[i] > base and digitlist[i] <= 3:
                        return i
                    if digitlist[i] > 3:
                        return -1
            return -1
        if k == 3:
            for i in range(len(digitlist)):
                if digitlist[i] > base and digitlist[i] <= 5:
                    return i
                if digitlist[i] > 5:
                    return -1
            return -1
        if k == 4:
            for i in range(len(digitlist)):
                if digitlist[i] > base:
                    return i
            return -1           
                
obj = Solution()
time = "18:42"    
print(obj.nextClosestTime(time)) 
            
            
            
                
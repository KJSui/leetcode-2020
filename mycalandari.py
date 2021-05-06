class MyCalendar:
    
    def __init__(self):
        self.cl = []        
        
    def book(self, start, end):
        s = 0
        e = len(self.cl)-1
        while s < e:
            print("list: ", self.cl)
            print("\n")
            mid = s + int((e-s)/2)
            if self.cl[mid][0] <= start:
                s = mid+1
            elif self.cl[mid][0] > start:
                e = mid
            else:
                return False
            print("mid: ", mid, "s: ", s, "e: ", e)
            print("\n")
        if len(self.cl) == 0:
            self.cl.append([start, end])
            return True

        if s > e and e >= 0:
            if self.cl[s][0] >= end and self.cl[e][1] <= start :
                self.cl.insert(s+1, [start, end])
                return True
            return False
        else:
            if self.cl[s][1] <= start:
                if s+1 < len(self.cl):
                    if self.cl[s+1][0] < end:
                        return False
                self.cl.insert(s+1, [start, end])
                return True
            if self.cl[s][0] >= end:
                if s-1>=0:
                    if self.cl[s-1][1] > start:
                        return False
                self.cl.insert(s, [start, end])
                return True                
            return False
            


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()

k = [[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
for i in k:
    print("===========[start, ", i[0], "end: ", i[1], "]========")
    print("\n")
    param_1 = obj.book(i[0],i[1])
    print("booking: ", param_1)
    print("\n")
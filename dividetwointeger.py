class Solution:
    def divide(self, d1, d2):
        pos = 1
        if d1 > 0 and d2 > 0 or d1 < 0 and d2 < 0:
            pos = 1
        else:
            pos = -1
        res = 0
        while d1 >= d2:
            k = d2
            count = 1
            while k <= d1:
                d1 -= k 
                res += count 

                k = k << 1
                count = count << 1

        return res * pos
class Solution:
    def findUnion(self, a, b):
        if len(a) == 0 or len(b) == 0:
            return [] 
        if a[0] < b[0]:
            a, b = b, a 
        res = []
        for i in a:
            k = self.binarySearch(b, i)
            print("k value: ", k, "i in a: ", i, "b: ", b)
            if b[k] == i:
                res.append(i)
            b = b[k+1:]
            if len(b) == 0:
                return res 
        return res 



    def binarySearch(self, array, v):
        l = 0
        r = len(array)-1

        while l < r:
            m = (l+r)//2
            if array[m] == v:
                return m 
            elif array[m] < v:
                l = m + 1
            else:
                r = m

        if l >= len(array) or array[l] > v:
            return l - 1
        return l  
a = [1, 4, 9, 12]
b = [2, 4, 11, 12, 15]

obj = Solution()
print(obj.findUnion(a, b))

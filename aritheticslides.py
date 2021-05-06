class Solution:
    def numberOfArithmeticSlices(self, A):
        res = 0
        if len(A) < 3:
            return 0
        
        i = 0
        while i < len(A):
            j = i+1
            if j == len(A):
                break
            gap = A[j] - A[i]
            while j < len(A) and A[j]- A[j-1] == gap:
                j += 1
            print("i:", i, " j:", j)
            if j == len(A) and j - i > 2:
                res += int((j-i+1 - 2)*(j-i - 2)/2)
                break
            
            if j < len(A) and j - 1 > 2:
                res += int((j-i+1-2)*(j-i-2)/2)
                i = j-1
                continue
                
            i += 1
        
        return res
obj = Solution()
A = [1,2,3,8,9,10]
print(obj.numberOfArithmeticSlices(A))
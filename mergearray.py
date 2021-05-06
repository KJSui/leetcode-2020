class Solution:
    def sortedSquares(self, A):
        valley = len(A)-1
        for i in range(len(A)):
            if A[i]*A[i] < A[valley]*A[valley]:
                valley = i
                print("vaalley: ", valley)
            A[i] = A[i]*A[i]
        print("AA:", A, "i: ", valley)
        if valley == 0:
            return A
        B = A[:valley]
        C = A[valley:]
        i = len(B)-1
        j = 0
        index = 0
        while i >= 0 and j < len(C):
            if B[i] > C[j]:
                A[index] = C[j]
                j += 1
            else:
                A[index] = B[i]
                i -= 1
            index += 1
            
        while i >= 0:
            A[index] = B[i]
            i -= 1
            index += 1
        while j < len(C):
            A[index] = C[j]
            j += 1
            index += 1
        
        return A
obj = Solution()
A = [2,3,3,4]
print(obj.sortedSquares(A))
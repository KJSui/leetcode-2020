class Solution:
    def longestOnes(self, A, K):
        left = 0
        for right in range(len(A)):
            K -= 1-A[right]
            if K < 0:
                K += 1 - A[left]
                left += 1
        return right - left + 1

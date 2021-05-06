class Solution:
    def sqrt(self, x):
        left = 0
        right = x 
        while left <= right:
            mid = left + (right-left)/2
            if x/mid < mid:
                right = mid - 1
            else:
                if x/(mid+1) < mid+1:
                    return mid 
                left = mid + 1
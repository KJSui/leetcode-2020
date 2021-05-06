class Solution:
    def findKthLargestInUnsortedArray(self, array, k):
        km = len(array)-k+1
        return self.quickselect(array, km)
    def quickselect(self, array, km):
        print("array:", array, "km:", km)
        if len(array) == 0:
            return -1
        if km == 1:
            return min(array)
        nb = self.pt(array, km)
        print("nb:", nb, "km:", km)
        if km > nb:
            return self.quickselect(array[nb:], km-nb)
        elif km == nb:
            return max(array[:nb])
        else:
            return self.quickselect(array[:nb], km)

    def pt(self, array, km):
        pivot = array[-1]
        start = 0
        end = len(array)-2
        while start < end:
            while start < end and array[start] < pivot:
                start += 1
            while start < end and array[end] >= pivot:
                end -= 1

            array[start], array[end] = array[end], array[start]
        
        array[start], array[-1] = array[-1], array[start]
        return start


obj = Solution()
array = [7, 10, 4, 3, 20, 15, 29, 6]
k = 4

print(obj.findKthLargestInUnsortedArray(array, k))
        


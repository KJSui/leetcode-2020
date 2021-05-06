class Solution:
    def quicksort(self, array, left, right):
        if left < right:
            pivot = self.partition(array, left, right)
            self.quicksort(array, left, pivot-1)
            self.quicksort(array, pivot+1, high)

    def partition(self, array, left, right):
        pivot = array[high]
        i = left 
        for j in range(left, high):
            if array[j] < pivot:
                array[i], array[j] = array[j], array[i]
                i += 1
        
        array[i], pivot = pivot, array[i]
        return i 

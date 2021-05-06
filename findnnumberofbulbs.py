class Solution:
    def kEmptySlots(self, bulbs, K):
        if len(bulbs) < 2:
            return -1
        array = [bulbs[0]]
        i = 1
        while i < len(bulbs):
            index = self.binarySearch(bulbs[i], array, 0, len(array)-1)
            print("index: ", index)
            print("before array: ", array)
            if index > len(array)-1:
                if bulbs[i] - array[-1]-1 == K:
                    return i + 1
                array.append(bulbs[i])
            elif index < 0:
                if array[0] - bulbs[i] -1 == K:
                    return i+1
                array = [bulbs[i]] + array
            else:
                if array[index] - bulbs[i]-1 == K or bulbs[i]-array[index-1]-1 == K:
                    return i + 1
                array = array[:index] + [bulbs[i]] + array[index+1:]
            print("after array: ", array)
            i += 1

        return -1

    def binarySearch(self, v, array, left, right):
        mid = left + int((right-left)/2)
        if left >= len(array):
            return left
        if right < 0:
            return right
        if left > right:
            return mid
 
        if array[mid] > v:
            right = mid-1 
        elif array[mid] < v:
            left = mid + 1
        return self.binarySearch(v, array, left, right)

obj = Solution()
bulbs = [1,5,3]
K = 1
print(obj.kEmptySlots(bulbs, K))
        
        
        
            
        
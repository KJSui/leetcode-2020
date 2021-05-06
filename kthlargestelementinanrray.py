class Solution:
    def kthlargestElement(self, array, k):
        array = sorted(array)
        return self.select(array, 0, len(array)-1, len(array)-k)

    def partiton(self, left, right, array, pivot):
        pv = array[pivot]
        index = left
        pv, array[right] = array[right], pv
        for i in range(left, right+1):
            if array[i] < pv:
                array[index], array[i] = array[i], array[index]
                index += 1
        array[index], array[right] = array[right], array[index]
        return index

    def select(array, left, right, sk):
        if left == right:
            return array[left]
        pivot = random.randint(left, right)
        pivot = self.partition(left, right, array, pivot)
        if sk == pivot:
            return array[pivot]
        elif sk > pivot:
            return self.select(array, pivot+1, right, sk)
        else:
            return self.select(array, left, pivot-1, sk)


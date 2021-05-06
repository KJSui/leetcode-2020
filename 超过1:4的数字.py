class Solution:
    def findNumbers(self, array, k):
        start = 0
        total = len(array)
        nk = total//k
        res = []
        while start < len(array):
            value = array[start]
            idx = start + self.binarySearch(array[start:], value, 0)
            if array[idx] == value:
                idx += 1
            curr_len = idx - start
            if curr_len >= nk:
                res.append(value)
            if total - idx + 1 < nk:
                return res
            start = idx
        return res

    def binarySearch(self, array, value, left_check):
        l = 0
        r = len(array)-1
        while l <= r:
            mid = l + (r-l)//2
            if array[mid] == value:
                if left_check:
                    r = mid - 1
                else:
                    l = mid + 1
            elif array[mid] != value:
                if left_check:
                    l = mid + 1
                else:
                    r = mid - 1
        if left_check:
            return l
        else:
            return r
obj = Solution()
array = [2, 2, 2, 2, 2, 2, 3, 3, 3]
k = 1
print(obj.findNumbers(array, k))

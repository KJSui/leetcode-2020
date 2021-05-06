def binarySearch(self, num):
    l = 0
    r = len(num)-1
    while l + 1 < r:
        mid = l + (r-l)//2
        if num[mid] < target:
            l = mid 
        elif num[mid] > target:
            r = mid 
        else:
            return mid 

    if num[l] == target:
        return l

    if num[r] == target:
        return r
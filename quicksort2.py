class Solution:
    def quickSort(self, nums, k):
        if k > len(nums):
            return -1
        if k == len(nums):
            return max(nums)
        self.res = -1
        self.qsort(nums, 0, len(nums)-1, k)
        return self.res
    def qsort(self, nums, l, r, k):
        if k == 0:
            self.res = nums[l]
            return
        if l > r:
            return
        print("before: nums:", nums, "l:", l, "r:", r)
        pivot = self.partition(nums, l, r)
        print("after: nums:",nums, "l:", l, "r:", r, "pivot:", pivot)
        if pivot < k-1:
            self.qsort(nums, pivot+1, r, k)
        elif pivot == k-1:
            self.res = nums[pivot]
            return 
        else:
            self.qsort(nums, l, pivot-1, k)

    def partition(self, nums, l, r):
        pivot = r
        i = l  
        for j in range(l, r):
            if nums[j] < nums[pivot]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            
        nums[pivot], nums[i] = nums[i], nums[pivot]
        return i

obj = Solution()
nums = [2, 1, 9, 4, 5, 8, 10, 20, 6]
k = 6
print(obj.quickSort(nums, k))
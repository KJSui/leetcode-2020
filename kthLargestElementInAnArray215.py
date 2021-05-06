class Solution:
    def findKthLargest(self, nums, k):
        return self.select(nums, 0, len(nums)-1, len(nums)-k)
        
    def select(self, nums, left, right, k_smallest):
        if left >= right:
            return nums[left]
        pivot = random.randint(left, right)
        pivot = self.partition(nums, left, right, pivot)
        if pivot == k_smallest:
            return nums[k_smallest]
        elif pivot > k_smallest:
            return self.select(nums, left, pivot-1, k_smallest)
        else:
            return self.select(nums, pivot+1, right, k_smallest)

    def partition(self, nums, left, right, pivot):
        value = nums[pivot]
        value, nums[right] = nums[right], value
        idx = left
        for i in range(left,right):
            if nums[i] < value:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        nums[right], nums[idx] = nums[right], nums[idx]
        return idx

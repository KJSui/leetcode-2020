class Solution:
    def searchInRotatedArray(self, nums, target):
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            if (nums[0] <= target) is (nums[0] <= nums[mid]):
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid-1
            else:
                if nums[0] <= target:
                    right = mid-1
                else:
                    left  = mid + 1

        return -1

obj = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(obj.searchInRotatedArray(nums, target))

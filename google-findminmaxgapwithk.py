#find a longest sublist which the max - min value <= k:
from collections import deque

def longest_subarray_with_d(nums, d):
    min_deque = deque([])
    max_deque = deque([])
    left, right = 0, 0
    rst = 0

    while right < len(nums):
        while min_deque and min_deque[-1] > nums[right]:
            min_deque.pop()
        min_deque.append(nums[right])

        while max_deque and max_deque[-1] < nums[right]:
            max_deque.pop()
        max_deque.append(nums[right])

        right += 1

        while max_deque and min_deque and max_deque[0] - min_deque[0] > d:
            if nums[left] == max_deque[0]:
                max_deque.popleft()

            if nums[left] == min_deque[0]:
                min_deque.popleft()

            left += 1

        rst = max(rst, right-left)
    return rst
print(longest_subarray_with_d([2,1,10, 11, 13, 3], 3))
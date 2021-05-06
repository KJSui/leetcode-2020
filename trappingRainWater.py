class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        leftHighest = 0
        rightHighest = 0
        left = 0
        right = len(height)-1
        res = 0
        while left < right:
            if height[left] < height[right]:
                if leftHighest > height[left]:
                    res += leftHighest-height[left]
                else:
                    leftHighest = height[left]
                left += 1
            else:
                if rightHighest > height[right]:
                    res += rightHighest - height[right]
                else:
                    rightHighest = height[right]
                right -= 1
        return res
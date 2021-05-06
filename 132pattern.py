class Solution:
    def find132pattern(self, nums):
        i = 0
        sk1 = []
        minstack = []
        low = 0
        while i < len(nums):
            if nums[low] >= nums[i]:
                minstack.append(nums[i])
                low = i
            else:
                minstack.append(nums[low])
            i += 1

        i = len(nums)-1
        while i >= 0:
            if len(sk1) == 0:
                sk1.append(nums[i])
                i -= 1
                continue

            
            if nums[i] == minstack[i]:
                i -= 1
                while len(sk1) > 0 and i >= 0 and nums[i] >= minstack[i] and sk1[-1] <= minstack[i]:
                    sk1.pop()
                if i >= 0 and len(sk1) > 0 and sk1[-1] < nums[i]:
                    return True
                sk1.append(nums[i]) 
                continue
                
            if len(sk1) > 0 and nums[i] > sk1[-1] and sk1[-1] > minstack[i]:
                    return True
                
            sk1.append(nums[i])
            i -= 1
    
        return False

obj = Solution()
nums = [3, 1, 2]
print(obj.find132pattern(nums))
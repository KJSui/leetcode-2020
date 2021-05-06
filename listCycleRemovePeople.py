class Node:
    def __init__(self, val):
        self.next = None 
        self.val = val 

class Solution:
    def removePeople(self, nums):
        if len(nums) <= 1:
            return []
        if len(nums) <= 3:
            return nums[1]
        
        head = headstart = Node(nums[1])
        start = 3
        while start < len(nums):
            head.next = Node(nums[start])
            head = head.next 
            start += 2
        head.next = None 

        if start == len(nums)+1:
            if headstart.next == None:
                return headstart.val 
            headstart = headstart.next 
        head = headstart

        while  headstart and headstart.next:
            while head and head.next:
                tmp = head.next
                head.next = tmp.next 
                tmp.next = None 
                head = head.next
            if head == None:
                head = headstart
            elif head.next == None:
                head = headstart.next 
                headstart.next = None 
                headstart = head

        return headstart.val 

obj = Solution()
nums = [1, 2, 3, 4, 5, 6]
print(obj.removePeople(nums))



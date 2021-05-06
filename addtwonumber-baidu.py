class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumber(self, l1, l2):
        carry = 0
        sumv = 0
        last_node_l1 = l1
        last_node_l2 = l2
        head = l1
        while l1 and l2:
            sumv = l1 + l2 + carry
            if(sumv >= 10)
                carry = 1
                sumv -= 10
            else:
                carry = 0
            l1.val = sumv

            l1 = l1.next
            l2 = l2.next
            if(l1 is None or l2 is None):
                break
            last_node_l1 = l1
            last_node_l2 = l2

        while l1:
            sumv = l1.val + carry
            if sumv > 9:
                carry = 1
                sumv -= 10
            else:
                carry = 0
            l1.val = sumv
            l1 = l1.next

        l1 = last_node_l1
        last_node_l2.next = None
        while l2:
            sumv = l2.val + carry
            if sumv > 9:
                carry = 1
                sumv -= 10
            else:
                carry = 0
            l1.next = l2
            l1 = l1.next
            l1.val = sumv
            l2 = l2.next

        return head ßß 

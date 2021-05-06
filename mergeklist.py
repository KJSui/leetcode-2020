class Solution:
    def mergeKlists(self, lists):
        length = len(list)
        interval = 1
        while interval < length:
            for i in range(0, length-interval, interval*2):
                lists[i] = self.merge2lists(lists[i], lists[i+interval])
            interval *= 2

        return lists[0] if length > 0 else None


    def merge2lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next

            else:
                point.next = l2
                l2 = l2.next

            point = point.next 


        if not l1:
            point.next = l2

        if not l2:
            point.next = l1

        return head.next
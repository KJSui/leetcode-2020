class Solution:
    def mergeKLists(self, lists):
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount-interval, interval*2):
                lists[i] = self.merge2lists(lists[i], lists[i+1])
            interval *= 2

        return lists[0] if amount > 0 else None

    def merge2lists(self, l1, l2):
        head = point = listNode(0)
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
        else:
            point.next = l1

        return head.next

class Solution:
    def randomPointCopy(self, head):
        if head is None:
            return head

        if head in self.visited:
            return self.visited[head]

        node = Node(head.val, None, None)
        self.visited[head] = node

        node.random = self.randomPointCopy(head.random)
        node.next = self.randomPointCopy(head.next)

        return node
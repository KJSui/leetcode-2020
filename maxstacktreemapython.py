from sortedcontainers import SortedDict

class Solution:
    def __init__(self):
        self.dlist = DList()
        self.treemap = SortedDict()

    def push(self, x):
        node = self.dlist.add(x)
        if x in self.treemap:
            self.treemap[x].apend(node)
        else:
            self.treemap[x] = [node]

    def pop(self):
        node = self.dlist.pop()
        self.treemap[node.val].pop()
        if len(self.treemap[node.val]) == 0:
            del self.treemap[node.val]

        return node.val

    def top(self):
        return self.dlist.peek()

    def peekMax(self):
        return self.treemap.keys()[-1]

    def popMax(self):
        max_key = self.treemap.keys()[-1]
        node = self.treemap[max_key][-1]
        self.treemap[max_key].pop()
        if len(self.treemap[max_key]) == 0:
            del self.treemap[max_key]

        self.dlist.remove(node)

        return max_key

class Dnode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DList:
    def __init__(self):
        self.head = Dnode(0)
        self.tail = Dnode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def pop(self):
        return self.remove(self.tail.prev)

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.pre
        return node

    def add(self, val):
        node = Dnode(val)
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        return node 

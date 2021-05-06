class DlinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DlinkedNode(), DlinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node

    def _remove_node(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        prev = self.tail.prev
        self._remove_node(prev)
        return prev

    def get(self, key):
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)

    def put(self, key, value):
        node = self.cache.get(key)
        if not node:
            newNode = DlinkedNode(）
            newNode.key = key
            newNode.value = value
            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1

        else:
            node.value = value
            self._move_to_head(node)
            

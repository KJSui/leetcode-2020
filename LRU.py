class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash_map = {}

        self.head = None
        self.end = None 

        self.curr_size = 0

    def get(self, key):
        if key not in self.hash_map:
            return -1 
        node = self.hash_map[key]
        if self.head == node:
           return node.value 
        self.remove(node)
        self.set_head(node)
        return node.value 

    def remove(self, node):
        if not self.head:
            return 
        if node.prev:
            node.prev.next = node.next 
        if node.next:
            node.next.prev = node.prev 

        if not node.next and not node.prev:
            self.head = None 
            self.end = None 

        if self.end == node:
            self.end = node.next 
            self.end.prev = None 
        self.curr_size -= 1

        del self.hash_map[node.key]
        return node 

    def set_head(self, node):
        if not self.head:
            self.head = node 
            self.end = node 
        else:
            node.prev = self.head 
            self.head.next = node
            self.head = node 
        self.curr_size += 1

    def set(self, key, value):
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value

            if self.head != node:
                self.remove(node)
                self.set_head(node)
        else:
            new_node = Node(key, value)
            if self.curr_size == self.capacity:
                del self.hash_map[self.end.key]
                self.remove(self.end)
            self.hash_map[key] = new_node
            self.set_head(node)

            
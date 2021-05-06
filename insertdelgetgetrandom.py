class Solution:
    def __init__(self):
        self.list = []
        self.mp = {}

    def insert(self, val):
        if val in self.map.keys():
            return False
        self.list.append(val)
        self.map[val] = len(self.list)-1
        return True

    def remove(self, val):
        if val not in self.map.keys():
            return False

        index = self.map[val]
        if index == len(self.list)-1:
            self.list.pop()
            del self.map[val]

        else:
            last = self.list.pop()
            self.map[last] = index
            self.list[index] = last
            del self.map[val]

        return True

    def getRandom(self):
        return choice(self.list)
        

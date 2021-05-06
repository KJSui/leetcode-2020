class NestedIterator(object):
    def __init__(self, nestedList):
        self.idx = 0
        self.stack = []
        self.curr = nestedList[self.idx]
    def next(self):
        if type(self.curr) == type(1):
            if len(self.stack) == 0:
                self.idx += 1
                self.curr = nestedList[self.idx]
            else:
                self.curr = self.stack.pop()
            return self.curr
        else:
            for i in range(len(self.curr)-1, -1, -1):
                self.stack.append(self.curr[i])
            self.curr = self.stack.pop()
            return self.next()
    def hasNext(self):
        if self.idx == len(nestedList):
            return False
        return True

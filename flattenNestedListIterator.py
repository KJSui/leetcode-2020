class NestedIterator(object):
    def __init__(self, nestedList):
        self.stack = []
        self.input = nestedList 
        self.index = 0
        self.tmp = nestedList[self.index]

    def next(self):
        if type(self.tmp) == type(1):
            if len(stack) == 0:
                self.index += 1
                self.tmp = self.input[self.index]

            else:
                self.tmp = self.stack.pop()

            return self.tmp 

        else:
            k = self.tmp 
            for i in range(len(k)-1, -1, -1):
                self.stack.append(k[i])

            self.tmp = self.stack.pop()

            return self.next()
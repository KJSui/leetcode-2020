class Solution:
    def __init__(self):
        self.minstack = []
        self.stack = []

    def push(self, x):
        self.stack.append(x)
        if len(self.minstack) == 0 or x < self.getMin():
            self.minnstack.append(x)


    def pop(self):
        x = self.stack.pop()
        if x == self.getMin():
            self.minstack.pop()

    def getMin(self):
        return self.minstack[-1]

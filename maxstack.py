class maxStack(list):
    def __init__(self):
        self.stack = []
    def push(self, x):
        if len(self.stack):
            m = max(m, self.stack[-1])
        self.stack.append((x, m))

    def pop(self):
        return self.stack.pop()[0]

    def top(self):
        return self.stack[-1][0]

    def peekMax(self):
        return self.stack[-1][1]

    def popMax(self):
        m = self.stack[-1][1]
        b = []
        while self.stack[-1][0] != m:
            b.append(self.pop())

        self.pop()
        map(self.push, reversed(b))
        return m
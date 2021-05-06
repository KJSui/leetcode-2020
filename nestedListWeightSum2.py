class Solution:
    def depthSumInverse(self, nestedList):
        stack = collections.deque([])
        self.flat(nestedList, stack, 1)
        if not self.stack:
            return 0
        return self.calculate(stack)


    def flat(self, nestedList, stack, count):
        for i in nestedList:
            if i.isInteger():
                stack.appendleft((i.getInteger(), count))
            else:
                self.flat(i.getList(), stack, count+1)

    def calculate(self, stack):
        max_depth = max(item[1] for item in stack)
        res = 0
        for val, count in stack:
            res += val * (max_depth+1-count)

        return res


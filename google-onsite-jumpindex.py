import collections
class Solution:
    def findShortestPathToend(self, array):
        self.mp = collections.defaultdict(list)
        for i, j in enumerate(array):
            self.mp[j].append(i)
        print("mp:", self.mp)
        self.res = []
        self.visited = set()
        self.helper(array, 0, [])
        return self.res

    def helper(self, array, start, lt):
        if start == len(array)-1:
            if len(self.res) == 0 or len(self.res) > len(lt):
                self.res = lt[:]
            return
        if start in self.visited:
            return
        self.visited.add(start)
        queue = []
        if start > 0 and start-1 not in self.visited:
            queue.append(start-1)
        if start < len(array) and start + 1 not in self.visited:
            queue.append(start+1)
        print("first queue:", queue)
        tmplist = self.mp[array[start]]
        print("tmplist:", tmplist)
        queue = queue + tmplist
        print("queue:", queue)
        for i in queue:
            self.helper(array, i, lt + [i])
        if start in self.visited:
            self.visited.remove(start)
        return

obj = Solution()
array = [1, 4, 3, 7, 5, 2, 4, 6]
print(obj.findShortestPathToend(array))
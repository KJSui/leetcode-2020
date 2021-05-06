class Solution:
    def arrayTreeNode(self, array, id):
        self.mp = defauldict(list)
        queue = []
        for i in range(len(array)):
            if array[i] == i:
                queue.append(i)
            
        while queue:
            index = queue.pop(0)
            for i in range(len(array)):
                if array[i] == index:
                    queue.append(i)
                    self.mp[index].append(i)
        
    def input()

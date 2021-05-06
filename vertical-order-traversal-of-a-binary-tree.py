class Solution:
    def vertical-order-traversal-of-a-binary-tree(self, root):
        self.res = collections.defaultdict(lambda: collections.defaultdict(list))
        self.dfs(root, 0, 0)
        final = []
        for i in sorted(self.res):
            report = []
            for j in sorted(self.res[i]):
                report.extend(sorted(v for v in self.res[i][j]))
            final.append(report)
        return final 
                
    def dfs(self, root, x, y):
        if not root:
            return 
        self.res[x][y].append(root.val)
        self.dfs(root.left, x-1, y+1)
        self.dfs(root.right, x+1, y+1)

    
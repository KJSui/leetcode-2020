def dfs(self, root, x=0, y=0):
    if root:
        seen[x][y].append(root.val)
        self.dfs(root.left, x-1, y+1)
        self.dfs(root.right, x+1, y+1)

    
def verticalTraversal(self, root):
    seen = collections.defaultdict(lambda: collections.defaultdict(list))
    dfs(root)
    ans = []

    for x in sorted(seen):
        report = []
        for y in sorted(seen[x]):
            report.extend(sorted(node.val for node in seen[x][y]))
        ans.append(report)

    return ans 

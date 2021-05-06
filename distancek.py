class Solution:
    def distanceK(self, root, target, K):


    def dfs(self, node, par=None):
        if node:
            node.par = par
            self.dfs(node.left, node)
            self.dfs(node.right, node)

    dfs(root)
    queue = collections.deque([(target, 0)])
    seen = {target}
    while queue:
        if queue[0][1] == K:
            return [node.val for node, d in queue]
        else:
            node, d = queue.popleft()
            for neigh in (node.left, node.right, node.par):
                if neigh and neigh not in seen:
                    seen.add(neigh)
                    queue.append((neigh, d+1))

    return []

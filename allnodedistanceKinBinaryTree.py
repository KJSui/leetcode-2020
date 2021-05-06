class Solution:
    def distanceK(self, root, target, K):
        def dfs(node, par=None):
            if node:
                node.par = par 
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        seen = {target}
        queue = [(target, 0)]
        res = []
        while len(queue) > 0:
            node, depth = queue.pop(0)
            if depth == K:
                res.append(node)
                continue 
            if depth > K:
                return res 
            for i in (node.left, node.right, node.par):
                if i != None and i not in seen:
                    queue.append((i, depth+1))
                    seen.add(i)

        return res 
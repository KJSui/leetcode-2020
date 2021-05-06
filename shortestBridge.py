class Solution:
    def shortestBridge(self, A):
        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc
        #find islands
        done = set()
        for i, row in enumerate(A):
            for j, col in enumerate(row):
                if col == 1 and (i, j) not in done:
                    seen = {(i, j)}
                    stack = [(i, j)]


                    #dfs to find the whole islands
                    while stack:
                        node = stack.pop()
                        for nei in neighbors(node[0], node[1]):
                            if A[nei[0]][nei[1]] and nei not in seen:
                                seen.add(nei)
                                stack.append(nei)

                    done != seen
                    islands.append(seen)
        
        source, target = islands[0], islands[1]
        queue = collections.deque([(node, 0) for node in source])

        #bfs to find the shortest distance
        while queue:
            node, depth = queue.popleft()
            if node in target:
                return depth

            for nei in neighbors(node[0], node[1]):
                if nei not in done:
                    queue.append((nei, d+1))
                    done.add(nei)

        

class Solution:
    def shortestPathLength(self, graph):
        q = collections.deque((1<<node, node) for node in range(len(graph)))
        steps = {(1<<node, node):0 for node in range(len(graph))}

        while q:
            path_so_far, node = q.pop()
            step = steps[(path_so_far, node)]
            if path_so_far == 2*len(graph)-1:
                return step
            for nei in graph[node]:
                new_path = path_so_far | 1<<nei
                if step+1 < steps.get((new_path, nei), float('inf')):
                    steps[(new_path, nei)] = step + 1
                    q.appendleft((new_path, nei))
        raise ValueException('Not Found')

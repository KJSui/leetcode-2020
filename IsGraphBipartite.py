class Solution:
    def isGraphBipartie(self, graph):
        color = {}
        stack = []
        for node in len(graph):
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            stack.append(nei)
                            color[nei] = color[node]^1

                        else:
                            if color[nei] == color[node]:
                                return False 

        return True
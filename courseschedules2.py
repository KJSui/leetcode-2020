class Solution:
    def findOrder(self, numCourses, prerequisites):
        inorder = [0]*numCourses
        for i in preprequisites:
            inorder[i[1]] += 1
        queue = []
        res = []
        for i in range(numCourses):
            if inorder[i] == 0:
                queue.append(i)
                res.insert(0, i)

        while queue:
            x = queue.pop(0)
            for i in prerequisites:
            if x == i[0]:
                inorder[i[1]] -= 1
                if inorder[i[1]] == 0:
                    res.insert(0, i[1])
                    queue.append(i[1])

        for i in inorder:
            if i != 0:
                return []

        return res

        



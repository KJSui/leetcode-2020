class Solution:
    def canFinish(self, numCourses, prerequisites):
        inDegree = [0]*numCourses
        for i in prerequisites:
            if inDegree[i[1]] += 1

        queue = []
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                queue.append(i)

        while len(queue) > 0:
            num = queue.pop(0)
            for i in prerequisites:
                if k == i[0]:
                    inDegree[i[1]] -= 1
                    if inDegree[i[1]] == 0:
                        queue.append(inDegree[i[1]])

        for i in inDegree:
            if i != 0:
                return False

        return True
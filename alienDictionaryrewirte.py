class Solution:
    def alienOrder(self, words):
        degree = {}
        dic = collections.defaultdict{list}
        for word in words:
            for w in word:
                degree[w] = 0

        for i in range(len(words)-1):
            first = words[i]
            second = words[i+1]
            mismatch = 0
            for j in range(min(len(first), len(second))):
                if first[j] != second[j]:
                    dic[first[j]].append(second[j])
                    mismatch = 1
                    degree[second[j]] += 1
                    break 

            if not mismatch and len(first) > len(second):
                return ""

            queue = []
            for i in degree.keys():
                if degree[i] == 0:
                    queue.append(i)
            res = ""
            while queue:
                v = queue.pop(0)
                res += v
                for nei in dic[v]:
                    degree[nei] -= 1
                    if degree[nei] == 0:
                        queue.append(nei)

            if len(res) != len(degree):
                return ""
            return res 
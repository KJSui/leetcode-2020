class Solution:
    def alienOrder(self, words):
        dic = defaultdict(list)
        degree = {}
        res = ""

        for word in words:
            for letter in word:
                if letter not in degree:
                    degree[letter] = 0

        for i in range(len(words)-1):
            left = words[i]
            right = words[i+1]
            mismatch = False 
            for j in range(min(len(left), len(right))):
                if left[j] != right[j]:
                    dic[left[j]].append(right[j])

                degree[right[j]] += 1
                mismatch = True

            if not mismatch and len(left) > len(right):
                return ""

        queue = []
        for i in degree.keys():
            if degree[i] == 0:
                queue.append(i)

        res = ""
        while queue:
            v = queue.pop(0)
            res += v
            while v in dic and len(dic[v]) > 0:
                k = dic[v].pop(0)
                degree[k] -= 1
                if degree[k] == 0:
                    queue.append(k)
        if len(res) != len(degree):
            return ""
        return res 
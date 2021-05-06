class Solution:
    def alienword(self, words):
        diction = {}
        res = ""
        degree = {}
        for i in range(len(words)-1):
            left = words[i]
            right = words[i+1]
            for j in range(min(len(left), len(right))):
                if left[j] != right[j]:
                    if left[j] not in diction:
                        diction[left[j]] = [right[j]]
                    else:
                        diction[left[j]].append(right[j])
                    degree[right[j]] += 1
                    mismatch = 1sss
                    break
                else:
                    continue
            if not mismatch and len(right) > len(left):
                return ""

        queue = []
        for i in degree.keys():
            if degree[i] == 0:
                queue.append(i)
        while queue:
            top = queue.pop(0)
            res += top
            while top in diction and len(diction[top]) > 0:
                k = diction[top].pop(0)
                degree[k] -= 1
                if degree[k] == 0:
                    queue.append(k)
        if len(res) != len(degree):
            return ""
        return res

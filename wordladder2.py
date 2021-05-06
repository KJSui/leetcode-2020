from collections import defaultdict
class Solution:
    def wordladder2(self, begin, end, lt):
        l = len(begin)
        dt = defaultdict(list)
        if end not in lt or not end or not begin or not lt:
            return []
        res = []
        dontgo = set([])
        for word in lt:
            for i in range(l):
                dt[word[:i]+"*"+word[i+1:]].append(word)

        queue = []
        for i in range(l):
            for w in dt[begin[:i]+"*"+begin[i+1:]]:
                if w != begin:
                    queue.append((w, [begin], 1))
                    dontgo.add(begin)
        maxl = len(lt)+1

        while queue:
            w, oldpath, n = queue.pop(0)
            path = oldpath.copy()
            path.append(w)
            dontgo.add(w)
            n += 1
            if n > maxl:
                continue
            if w == end:
                if n < maxl:
                    res = [path]
                    maxl = n
                elif n == maxl:
                    res.append(path)
            for i in range(l):
                for word in lt[w[:i]+"*"+w[i+1:]]:
                    if word not in path and word not in dontgo:
                        queue.append((word,path, n))

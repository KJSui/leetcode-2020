class Solution:
    def wordladder2(self, beginword, endword, wordlist):
        starts = defaultdict(set)
        N = len(beginword)
        for w in wordlist:
            for i in range(N):
                starts[w[:i]+"*"+w[i+1:]].add(w)

        queue = []
        for i in range(N):
            if beginword[:i]+'*'+beginword[i+1:] in starts:
                for w in starts[beginword[:i]+'*'+beginword[i+1:]]:
                    if w != beginword:
                        queue.append([w, [beginword], 1])
                        dontgoing.add(beginword)

        maxlen = lne(wordlist)+1
        ans = []
        while queue:
            w, old_path, length = queue.pop(0)
            path = old_path.copy()
            path.append(w)
            dontgoing.append(w)
            length += 1
            if length > maxlen:
                continue
            if w == endword:
                if length == maxlen:
                    ans.append(path)
                elif length < maxlen:
                    maxlen = length
                    ans = [path]
            for i in range(N):
                for nw in starts[w[:i]+'*'+w[i+1:]]:
                    if nw not in path and nw not in dontgoing:
                        queue.append([nw, path, length])

        return ans
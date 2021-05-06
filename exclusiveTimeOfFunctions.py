class Solution:
    def exclusiveTime(n, logs):
        res = [0] * n
        stack = []
        if len(logs) == 0:
            return []
        s = logs[0].split(':')
        stack.append(int(s[0]))
        i = 1
        prev = int(s[2])
        while i < len(logs):
            k = logs[i].split(':')
            if k[1] == 'start':
                if len(stack) > 0:
                    res[stack[-1]] += int(k[2]) - prev
                stack.append(int(k[0]))
                prev = int(k[2])

            else:
                res[stack[-1]] += int(k[2]) - prev + 1
                stack.pop()
                prev = int(k[2])+1
            i += 1

        return res

def Solution:
    def minWindowSubstring(self, s, t):
        t_dict = {}
        for i in t:
            t_dict[i] = t_dict.get(i, 0)+1

        t_len = len(t)

        window = {}

        s_array = []
        for i, j in enumerate(s):
            if j in t_dict:
                s_array.append((i, j))

        l = r = 0
        form = 0
        ans = (float('inf'), 0, 0)
        while r < len(s_array):
            char = s_array[r][1]
            window[char] = window.get(char, 0)+1
            if window[char] == t_dict[char]:
                form += 1
            while form == t_len and l <= r:
                char2 = s_array[l][1]
                start = s_array[l][0]
                end = s_array[l][1]
                if end - start + 1 < ans[0]:
                    ans = (end-start+1, start, end)

                window[char] -= 1
                if window[char] < t_dict[char]:
                    form -= 1
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
                
            
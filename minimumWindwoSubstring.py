class Soution:
    def minWindow(self, s, t):
        t_dict = {}
        for i in t:
            if i not in t_dict:
                t_dict[i] = 1
            else:
                t_dict[i] += 1
        s_list = []
        for i in len(s):
            if s[i] not t_dict:
                continue
            s_list.append([i, s[i]])

        window = {}
        start = 0
        formed = 0
        prev = 0
        res = float('inf'), None, None
        while start < len(s_list):
            c = s_list[start][1]
            window[c] = window.get(c, 0) + 1
            if window[c] == t_dict[c]:
                formed += 1
            while formed == len(t) and prev <= start:
                real_end = s_list[start][0]
                real_start = s_list[prev][0]
                real_len = real_end - real_start + 1
                if res[0] > real_len:
                    res = real_len, real_start, real_end
                 prev += 1
                 window[c] -= 1
                 if window[c] < t_dict[c]:
                     formed -= 1
            start += 1

        return "" if res[0] == float('inf') else s[res[1]:res[2]+1]

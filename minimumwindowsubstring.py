class Solution:
    def minWindow(self, s, t):
        dict_t = {}
        for i in t:
            if i not in dict_t:
                dict_t[i] = 1
            else:
                dict_t[i] += 1
        
        window = []
        for i in range(len(s)):
            if i in dict_t:
                window.append((i, s[i]))
        
        pending = 0
        required = len(t)

        check_dict = {}

        ans = len(s)+1, None, None
        l = r = 0
        while r < len(window):
            c = window[r][1]
            check_dict[c] = check_dict.get(c, 0)+1
            if check_dict[c] == dict_t[c]:
                pending+=1
            while pending == required and l <= r:
                end = window[r][0]
                start = window[l][0]
                if end - start + 1< ans[0]:
                    ans = (end-start+1, start, end)

                check_dict[c] -= 1
                if check_dict[c] < dict_t[c]:
                    pending -= 1
                
                l += 1
            r += 1

        return "" if ans[0] == len(s)+1 else s[ans[1]:ans[2]+1]
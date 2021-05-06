class Solution:
    def minumWindowSubstring(self, S, T):
        t_dir = {}
        for i in T:
            t_dir[i] = t_dir.get(i, 0)+1
        s_dir = {}
        window = [] 
        formed = 0
        start = end = 0
        res = float('inf'), 0, 0
        for i in range(len(S)):
            if S[i] in t_dir.keys():
                window.append((i, S[i]))
            
        while end < len(window):
            charv = window[end][1]
            s_dir[charv] = s_dir.get(charv, 0)+1
            if s_dir[charv] == t_dir[charv]:
                formed += 1
            while start <= end and formed == len(t_dir):
                end_index = window[end][0]
                start_index = window[start][0]
                if end_index - start_index+1 < res[0]:
                    res = (end_index-start_index+1, start_index, end_index)

                s_dir[S[start_index]] -= 1
                if s_dir[S[start_index]] != t_dir[S[start_index]]:
                    formed -= 1
                     
                start += 1
            end += 1

            
class Solution:
    def expressiveWords(self, S, words):
        s_map = []
        start = 0
        s_set = set()
        while start < len(S):
            curr_w = S[start]
            c = start
            count = 0
            s_set.add(curr_w)
            while c < (len(S)) and S[c] == curr_w:
                count += 1
                c += 1
            s_map.append((curr_w, count))
            start = c
        print("s_map:", s_map)
        res = 0

        for w in words:
            i = 0
            flag = 0
            index = -1
            while i < len(w):
                if w[i] not in s_set:
                    flag = 1
                    break
                count = 0
                curr_c = w[i]
                index += 1
                while (i < len(w)) and (curr_c == w[i]):
                    count += 1
                    i += 1
                print("count:", count, "w[i-1]:", w[i-1], "word:", w)
                if count > s_map[index][1] or s_map[index][0] != curr_c:
                    flag = 1
                    break

                if count != s_map[index][1] and s_map[index][1] < 3:
                    flag = 1
                    break
            print("flag: ", flag, "index:", index, "len(s_map):", len(s_map))
            if i == len(w) and len(w) <= len(S) and flag == 0 and index+1 == len(s_map):
                print("current w:", w)
                res += 1
        return res
                        
obj = Solution()
S = "nnnnnnzzzznnnnnnpppppfffff"
words = ["nzznpf","nnzznnpff","nznpff","nnznnpf","nnznpff","nzznppf","nzznpff","nnzznnppf"]
print(obj.expressiveWords(S, words))


#corner case:
# S = "nnnzz", word = "nz"
# S = "nnnzznnnjj", word = "nznj"
# S= "leee", word = "leeee"
# S = "abccc", word = "abd"
# s = "abccc", word = "abcccd"


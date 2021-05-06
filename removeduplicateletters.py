class Solution:
    def removeDuplicateLetters(self, s):
        if len(s) == 0:
            return ""
        sk = [s[0]]
        mp = {}
        hashset = set(s[0])

        for i in s:
            if i not in mp:
                mp[i] = 1
            else:
                mp[i] += 1

        for i in range(1, len(s)):
            if s[i] > sk[-1]:
                hashset.add(s[i])
                sk.append(s[i])

            elif s[i] == sk[-1]:
                mp[s[i]] -= 1

            else:
                if s[i] not in hashset:
                    l = len(sk)
                    while l > 0:
                        if mp[sk[-1]] > 1:
                            if s[i] < sk[-1]:
                                tmp = sk.pop()
                                mp[tmp] -= 1
                                hashset.remove(tmp)
                                l -= 1
                            else:
                                break 
                        else:
                            break 
                    check.add(s[i])
                    sk.append(s[i])
                else:
                    mp[s[i]] -= 1
        return "".join(sk)



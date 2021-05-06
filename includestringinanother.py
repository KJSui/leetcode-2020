import collections
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        if len(s1) == len(s2):
            if sorted(s1) == sorted(s2):
                return True
            else:
                return False
        mp = {}
        mp2 = collections.defaultdict(list)
        for i in s1:
            if i not in mp.keys():
                mp[i] = 1
                mp2[i] = []
            else:
                mp[i] += 1
        print("23 mp:", mp, "mp2:", mp2)
        start = 0
        length = len(s1)
        lastprev = 0
        prev = 0
        curr = ""
        while start < len(s2):
            print("31:start:", start, "s2[start]:", s2[start])
            if s2[start] not in mp.keys():
                print("s2[start]:", s2[start])
                start += 1
                curr = ""
                length = len(s1)
                prev = start
            else:
                #duplicate
                print("mp2[s2[start]]", mp2[s2[start]])
                print("mp[s2[start]]:", mp[s2[start]])
                if len(mp2[s2[start]]) == mp[s2[start]]:
                    lastprev = prev
                    prev = mp2[s2[start]][0]
                    while lastprev <= prev:
                        if s2[lastprev] not in mp2.keys():
                            lastprev += 1
                            continue
                        mp2[s2[lastprev]].pop(0)
                        length += 1
                        curr = curr[1:]
                        lastprev += 1
                    length -= 1
                    mp2[s2[start]].append(start)
                    curr += s2[start]
                    prev += 1
                    start += 1


                elif len(mp2[s2[start]]) < mp[s2[start]]:
                    curr += s2[start]
                    length -= 1
                    mp2[s2[start]].append(start)
                    print("63 line: cur:", curr, "len:", length, "mp2[s2[start]]:", mp2[s2[start]])
                    start += 1
                    print("65:start:", start)
                if length == 0:
                    return True
        return False


obj = Solution()
s1 = "rmqqh"
s2 = "nrsqrqhrymf"
print(obj.checkInclusion(s1, s2))

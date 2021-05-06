class Solution:
    def permuationInString(self, s1, s2):
        s1_map = [0]*26
        s2_map = [0]*26

        for i in range(len(s1)):
            s1_map[ord(s1[i])-ord('a')] += 1
            s2_map[ord(s2[i])-ord('a')] += 1

        for i in range(len(s2)-len(s1)):
            if self.matched(s1_map, s2_map):
                return True

            s2_map[ord(s2[i+len(s1)]) - ord('a')] += 1
            s2_map[ord(s2[i]) - ord('a')] -= 1

        return self.matched(s1_map, s2_map)

    def matched(self, m1, m2):
        for i in range(26):
            if m1[i] != m2[i]:
                return False
        return True


        
class Solution:
    def printCommon(r1, r2):
        while 1:
            if r1:
                s1.append(r1)
                r1 = r1.left
            elif r2:
                s2.append(s2)
                r2 = r2.left

            elif len(s1) >0 and len(s2) > 0:
                r1 = s1[-1]
                r2 = s2[-1]

                if r1.key == r2.key:
                    print(r1.key)
                    s1.pop(-1)
                    s2.pop(-1)

                    r1 = r1.right
                    r2 = r2.right

                elif r1.key < r2.key:
                    s1.pop(-1)
                    r1 = r1.right

                    r2 = None

                elif r1.key > r2.key:
                    s2.pop(-1)
                    r2 = r2.right

                    r1 = None
            else:
                break
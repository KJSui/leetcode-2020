import collections
class Solution:
    def sortColor(self, array):
        a0 = collections.defaultdict(list)
        a1 = collections.defaultdict(list)
        a2 = collections.defaultdict(list)

        c0 = 0
        c1 = 1
        c2 = 0

        swap = 0

        for i in array:
            if i == 0:
                c0 +=1
            elif i == 1:
                c1 += 1
            else:
                c2 += 1

        for i in range(len(array)):
            if i < c0:
                if array[i] == 1:
                    a0[1].append(i)
                elif array[i] == 2:
                    a0[2].append(i)

            elif i >= c0 and i < c0 + c1:
                if array[i] == 0:
                    a1[0].append(i)
                elif array[i] == 2:
                    a1[2].append(i)

            else:
                if array[i] == 0:
                    a2[0].append(i)
                elif array[i] == 1:
                    a2[1].append(i)

        i = j = 0
        while i < len(a0[1]) and j < len(a1[0]):
            array[a0[1][i]], array[a1[0][j]] = array[a1[0][j]], array[a0[1][i]]
            i += 1
            j += 1
            swap += 1
       
        i = j = 0
        while i < len(a0[2]) and j < len(a2[0]):
            array[a0[2][i]], array[a2[0][j]] = array[a2[0][j]], array[a0[2][i]]
            i += 1
            j += 1
            swap += 1
        
        i = j = 0
        while i < len(a1[2]) and j < len(a2[1]):
            array[a1[2][i]], array[a2[1][j]] = array[a2[1][j]], array[a1[2][i]]
            i += 1
            j += 1
            swap += 1
        print("swap: ", swap)
        return array
obj = Solution()
array = [0, 2, 1, 0, 1, 2, 0, 0, 2, 1, 0]

print(obj.sortColor(array))
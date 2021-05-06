class Solution:
    def findthreenumber(self, array):
        res = []
        for i in range(len(array)-1):
            if i == 0:
                res.append([array[i], max(array[i+1:])])
            else:
                leftmin = min(res[-1][0], array[i])
                rightmax = max(res[-1][1], array[i])
                if leftmin < array[i] and array[i] < rightmax:
                    return True
                res.append([leftmin, rightmax])
        return False

obj = Solution()
array = [8, 6, 2, 4]
print(obj.findthreenumber(array))

#在一个 int[] array , return 一个 boolean true, if there exists 0<=i<j<k< array.length, array[i] < array[j]< array[k].


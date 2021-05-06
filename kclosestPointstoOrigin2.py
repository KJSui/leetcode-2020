class Solution:
    def Kclosest(self, points, K):
        self.sort(0, len(points)-1, K, points)
        return points[:K]

    def dist(self, points, i):
        return points[i][0] ** 2 + points[i][1] ** 2

    def sort(self, i, j, K, points):
        if i >= j:
            return
        k = random.randint(i, j)
        points[i], points[k] = points[k], points[i]
        mid = self.partition(i, j, points)
        if K < mid-i+1:
            self.sort(i, mid-1, K, points)
        elif K > mid-i+1:
            self.sort(mid+1, j, K-(mid-i+1))

    def partition(self, i, j, points):
        ori = i
        pivot = self.dist(points, i)
        i += 1
        while True:
            while i < j and pivot > self.dist(points, i):
                i += 1
            while i <= j and self.dist(points, j) >= pivot:
                j -= 1

            if i >= j:
                break

            points[i], points[j] = points[j], points[i]
        points[ori], points[j] = points[j], points[ori]

        return j

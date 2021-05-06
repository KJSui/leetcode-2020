class Solution:
    def KClosest(self, points):
        dist = lambda x: points[x][0]**2 + points[x][1]**2
        def sort(i, j, K):
            if i >= j:
                return 
            k = randint(i, j)
            points[i], points[k] = points[k], points[i]

            mid = partition(i, j)
            if K < mid-i+1:
                sort(i, mid-1, K)
            elif K > mid-i+1:
                sort(mid+1, j, K-(mid-i+1))

        def partition(i, j):
            oi = i
            pivot = dist(i)
            i += 1
            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while j >= i and dist(j) >= pivot:
                    j -= 1
                if i >= j:
                    break 
                points[i], points[j] = points[j], points[i]
            points[oi], points[j] = points[j], points[oi]
            return j 
        sort(0, len(points)-1, K)
        return points[:K]
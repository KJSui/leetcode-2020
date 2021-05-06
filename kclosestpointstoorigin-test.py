class Solution:
    def kClosest(self, points, K):
        dist = lambda i: points[i][0**2 + points[i][1]*2
        def quicksort(start, end, K):
            if start >= end:
                return

            k = random.randint(start, end)
            points[start], points[k] = points[k], points[start]

            mid = partition(start, end)
            if K < mid-start+1:
                quicksort(start, mid-1, K)
            elif K > mid-start+1:
                quicksort(mid+1, j, K-(mid-i+1))

        def partition(i, j):
            oi = i
            pivot = dist(i)
            i += 1
            while True:
                while i < j and dist(i) < pivot:
                    i += 1

                while i <= j and dist(j) >= pivot:
                    j -= 1

                if i >= j:
                    break
                
                points[i], points[j] = points[j], points[i]

            points[oi], points[j] = points[j], points[oi]

            return j

        quicksort(0, len(points)-1, K)
        return points[:K]

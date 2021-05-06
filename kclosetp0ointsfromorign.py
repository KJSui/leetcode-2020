class Solution:
    def kCloset(self, points, K):
        dist = lambda x: points[x][0]**2 + points[x][1]**2

        def sort(i, j, K):
            if i >= j:
                return 
            pivot = random.randint(i, j)
            points[i], points[pivot] = points[pivot], points[i]

            mid = partition(i, j)
            if K < mid-i+1:
                sort(i, mid-1, K)
            elif K > mid-i+1:
                sort(mid+1, j, K-(mid_i+1))

        def partition(i, j):
            pivot = dist(i)
            start = i+1
            for k in range(i+1, j+1):
                if dist[k] < pivot:
                    points[k], points[start] = points[start], points[k]
                    start += 1

            points[i], points[start-1] = points[start-1], points[i]

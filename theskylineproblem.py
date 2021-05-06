import heapq
class Solution:
    def getSkyline(self, buildings):
        if len(buildings) == 0:
            return buildings
        
        res = []
        heights = []
        curr = []
        for b in buildings:
            heights.append([b[0], -b[2]])
            heights.append([b[1], b[2]])
        
        print("presortedd - heights: ", heights)
        heights.sort()
        print("heights: ", heights)
        preheight = 0
        for i in heights:
            if i[1] < 0:
                heapq.heappush(curr, i[1])
            else:
                curr.remove(-i[1])
            print("i th: ", i, "curr: ", curr)
            if len(curr) > 0:
                max_v = -curr[0]
                if preheight != max_v:
                    preheight = max_v
                    res.append([i[0], preheight])
            else:
                res.append([i[0], 0])
        return res
        
obj = Solution()
buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
print(obj.getSkyline(buildings))
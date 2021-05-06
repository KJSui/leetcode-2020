class Solution:
    def carFleet(self, target, position, speed):
        mp = {}
        i = 0
        for i in range(len(position)):
            mp[position[i]] = speed[i]
            
        position.sort(reverse=True)
        
        for i in range(len(speed)):
            speed[i] = mp[position[i]]    
        
        res = 0

        while len(position) > 0:
            flag = 0
            i = 0
            while i < len(position):
                print("i value:\n", i)
                rd = position[i] + speed[i]
                position[i] = rd
                print("rd value:\n", rd)
                print(position)
                print(speed)
                if rd >= target:
                    flag = 1
                    position = position[:i] + position[i+1:]
                    speed = speed[:i] + speed[i+1:]
                    print("position:\n", position)
                    print("speed:\n", speed)
                else:
                    if i > 0 and rd >= position[i-1]:
                        position[i] = position[i-1]
                        speed[i] = speed[i-1]
                    i += 1
            if flag == 1:
                res += 1
                
        return res
obj = Solution()
target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
print(obj.carFleet(target, position, speed))
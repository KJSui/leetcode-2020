class Solution:
    def __init__(self):
        self.buffer = [""]*4
        self.offsite = 0
        self.bufferSize = 0
    def read(self, buf, n):
        flag = False
        total = 0
        while not flag and total < n:
            if self.buffSize == 0:
                self.bufferSize = read4(self.buffer)
                if self.bufferSize < 4:
                    flag = True
            byte = min(n-total, self.buffSize)
            for i in range(byte):
                buf[total] = self.buffer[self.offsite + i]
                total += 1

            self.offsite = (self.offsite+byte)%4
            self.buffSize -= byte

        return total 

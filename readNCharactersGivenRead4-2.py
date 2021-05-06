class Solution(object):
    def __init__(self):
        self.buffer = [0] * 4
        self.buffersize = 0
        self.offset = 0
    def read(self, buf, n):
        total = 0
        finished = False
        while not finished and total < n:
            if self.buffersize == 0:
                self.buffsize = read(self.buffer)
                if self.buffsize < 4:
                    finished = True
            actual = min(n-total, self.buffsize)
            for i in range(actual):
                buf[total] = self.buffer[i+self.offset]
                total += 1
            self.offset = (self.offset+actual)%4
            self.buffsize -= actual
        return total

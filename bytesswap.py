class Solution:
    def byteSwap(self, num):
        num = (num & 0x0000FFFF) << 16 | (num & 0xFFFF0000) >> 16
        num = (num & 0x00FF00FF) << 8 | (num & 0xFF00FF00) >> 8
        return num 
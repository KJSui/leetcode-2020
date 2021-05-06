class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        k = len(nums1)+len(nums2)
        if k%2 == 0:
            return (self.findKthNumber(nums1, 0, nums2, 0, int(k/2))+self.findKthNumber(nums1, 0, nums2, 0, int(k/2+1)))/2
        else:
            return self.findKthNumber(nums1, 0, nums2, 0, int(k/2)+1)
        
    def findKthNumber(self, nums1, start1, nums2, start2, k):
        if start1 >= len(nums1):
            return nums2[start2+k-1]
        if start2 >= len(nums2):
            return nums2[start1+k-1]
        if k == 1:
            return min(nums1[start1], nums2[start2])
        k1 = int(k/2)-1 + start1
        k2 = int(k/2)-1 + start2
        print("k1:", k1, "k2:", k2, "k:", k)

        if k1 < len(nums1):
            kv1 = nums1[k1]
        else:
            kv1 = float('inf')
        if k2 < len(nums2):
            kv2 = nums2[k2]
        else:
            kv2 = float('inf')
        print("kv1:", kv1, "kv2:", kv2)
        if kv1 < kv2:
            return self.findKthNumber(nums1, start1+int(k/2), nums2, start2, k-int(k/2))
        else:
            return self.findKthNumber(nums1, start1, nums2, start2+int(k/2), k-int(k/2))
        
        
obj = Solution()
nums1 = [1,3]
nums2 = [2]
print(obj.findMedianSortedArrays(nums1, nums2))
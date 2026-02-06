class Solution(object):
    def getCommon(self, nums1, nums2):


        nums1.sort()

        for n in nums1:
            if n in nums2:
                return n
        return -1        

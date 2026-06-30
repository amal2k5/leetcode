class Solution(object):
    def intersection(self, nums1, nums2):

        numsSet1 = set(nums1)
        numsSet2 = set(nums2)

        return list(numsSet1.intersection(numsSet2))

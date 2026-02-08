class Solution(object):
    def absDifference(self, nums, k):

        nums.sort()
        largest = sum(nums[-k:])
        smallest = sum(nums[:k])

        return largest - smallest



        
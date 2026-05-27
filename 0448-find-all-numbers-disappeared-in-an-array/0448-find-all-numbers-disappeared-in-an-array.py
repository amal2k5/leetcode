class Solution(object):
    def findDisappearedNumbers(self, nums):

        seen = set(nums)
        missingNums = []

        for n in range(1, len(nums) + 1):
            if n not in seen:
                missingNums.append(n)
        return missingNums        



        
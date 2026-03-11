class Solution(object):
    def missingNumber(self, nums):

        n = len(nums)
        s = set(nums)

        for num in range(n+1):
            if num not in s:
                return num

        
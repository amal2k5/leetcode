class Solution(object):
    def sumOfUnique(self, nums):

        once = [n for n in nums if nums.count(n) == 1]
        return sum(once)

        
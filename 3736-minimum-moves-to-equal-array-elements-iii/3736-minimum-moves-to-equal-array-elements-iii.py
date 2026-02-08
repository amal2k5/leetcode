class Solution(object):
    def minMoves(self, nums):

        max_value = max(nums)
        totalMoves = 0
        for n in nums:
            totalMoves += max_value - n
        return totalMoves    

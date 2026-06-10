class Solution(object):
    def canJump(self, nums):

        n = len(nums)
        goal = n-1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0      



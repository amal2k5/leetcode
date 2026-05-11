class Solution(object):
    def sortedSquares(self, nums):

        left = 0
        right = len(nums) - 1
        position = len(nums) - 1

        result = [0] * len(nums)
        
        while left <= right:
            left_squares = nums[left] * nums[left]
            right_squares = nums[right] * nums[right]

            if left_squares > right_squares:
                result[position] = left_squares
                left += 1
            else:
                result[position] = right_squares
                right -= 1

            position -= 1

        return result         

            

        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        nums = numbers
        right = len(nums)-1

        while left <= right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                return [left + 1, right + 1]

            elif current_sum > target:
                right -= 1

            elif current_sum < target:
                left += 1
                        

        
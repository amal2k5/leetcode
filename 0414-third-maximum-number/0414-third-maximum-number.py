class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        numbers = list(set(nums))
        numbers.sort()

        if len(numbers) <= 2:
            return numbers[-1]
        return numbers[-3]    
        
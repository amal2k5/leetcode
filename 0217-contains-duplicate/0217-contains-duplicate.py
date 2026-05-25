class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        for i in range(1, len(nums)):
            key = nums[i]
            j = i-1

            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key

            if j >= 0 and nums[j] == key:
                return True

        return False    

        
        
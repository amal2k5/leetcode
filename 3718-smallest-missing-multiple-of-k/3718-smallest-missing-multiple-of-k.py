class Solution(object):
    def missingMultiple(self, nums, k):

        numbers = nums
        currentNumber = k

        while currentNumber in numbers:
            currentNumber += k
        return currentNumber    

class Solution(object):
    def firstUniqueEven(self, nums):


        freq = {}

        for n in nums:
            freq[n] = freq.get(n,0) + 1

        for n in nums:
            if n % 2 == 0 and freq[n] == 1:
                return n
        return -1            

   

        
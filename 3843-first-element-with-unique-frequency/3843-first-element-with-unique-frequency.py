class Solution(object):
    def firstUniqueFreq(self, nums):

        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        freq_count = {}

        for c in freq.values():
            freq_count[c] = freq_count.get(c, 0) + 1

        for num in nums:
            if freq_count[freq[num]] == 1:
                return num

        return -1                
 
        
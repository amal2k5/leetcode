class Solution(object):
    def longestPalindrome(self, s):

        charFreq = {}

        for ch in s:
            charFreq[ch] = charFreq.get(ch, 0) + 1

        length = 0
        odd = False

        for count in charFreq.values():
            if count % 2 == 0:
                length += count
            else:
                length += count-1
                odd = True

        if odd:
            length += 1

        return length                    

        
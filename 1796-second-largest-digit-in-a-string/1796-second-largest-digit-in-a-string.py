class Solution(object):
    def secondHighest(self, s):

        digits = []

        for ch in s:
            if ch.isdigit() and int(ch) not in digits:
                digits.append(int(ch))

        if len(digits) < 2:
            return -1

        else:
            digits.sort()
            return digits[-2]                    




        
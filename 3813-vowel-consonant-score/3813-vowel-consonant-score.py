class Solution(object):
    def vowelConsonantScore(self, s):

        vows = 'aeiou'
        v = 0
        c = 0

        for ch in s:
            if ch in vows:
                v += 1
            elif ch.isalpha():
                c += 1

        score = 0
        if c > 0:
           score = v // c
        return score              

        
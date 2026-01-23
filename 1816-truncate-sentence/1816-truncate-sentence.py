class Solution(object):
    def truncateSentence(self, s, k):

        count = 0
        result = ''

        for ch in s:
            if ch == ' ':
                count += 1
            if count == k:
                break
            result += ch

        return result            

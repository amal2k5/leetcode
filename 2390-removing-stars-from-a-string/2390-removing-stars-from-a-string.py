class Solution(object):
    def removeStars(self, s):

        string = []

        for ch in s:
            if ch == '*':
                string.pop()
            else:
                string.append(ch)

        return ''.join(string)      

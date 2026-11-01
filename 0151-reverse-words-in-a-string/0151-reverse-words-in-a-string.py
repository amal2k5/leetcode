class Solution(object):
    def reverseWords(self, s):

        splitted = s.split()
        reversed = ' '.join(splitted[::-1])

        return reversed


class Solution(object):
    def reversePrefix(self, word, ch):

        idx = word.find(ch) + 1
        return word[:idx][::-1] + word[idx:]



        
class Solution(object):
    def greatestLetter(self, s):

        lowCase = set()
        upCase = set()

        for ch in s:
            if ch.islower():
                lowCase.add(ch)
            else:
                upCase.add(ch)

        for ch in reversed('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            if ch in upCase and ch.lower() in lowCase:
                return ch

        return ''                    

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        mapS2T = {}
        mapT2S = {}

        for cs, st in zip(s, t):

            if (cs in mapS2T and mapS2T[cs] != st) or (st in mapT2S and mapT2S[st] != cs):
                return False    

           
            mapS2T[cs] = st
            mapT2S[st] = cs

        return True



        
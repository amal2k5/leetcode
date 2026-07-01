class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        ST_mapper = {}
        TS_mapper = {}  

        for S_ch, T_ch in zip(s, t):

            if S_ch in ST_mapper and ST_mapper[S_ch] != T_ch:
                return False
            
            if T_ch in TS_mapper and TS_mapper[T_ch] != S_ch:
                return False

            ST_mapper[S_ch] = T_ch
            TS_mapper[T_ch] = S_ch    

        return True        

        
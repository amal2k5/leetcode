class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dict1 = {}
        res = 0
        for i in arr:
            dict1[i] = dict1.get(i,0)+1
        for k ,v in dict1.items():
            if k == v and res < v:
                res = k  
        return res if res > 0 else -1
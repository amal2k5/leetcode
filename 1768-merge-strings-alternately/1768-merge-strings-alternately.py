class Solution(object):
    def mergeAlternately(self, word1, word2):
        length1 = len(word1) 
        length2 = len(word2)  
        
        result = ""
        
        for i in range(min(length1, length2)):
            result += word1[i] + word2[i]
        
        if length1 > length2:
            result += word1[length2:]
        elif length2 > length1:
            result += word2[length1:]
        
        return result
        
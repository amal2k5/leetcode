class Solution(object):
    def stringMatching(self, words):

        n = len(words)
        result = set()

        for i in range(n):
            for j in range(n):

                if i != j and words[j] in words[i]:
                    result.add(words[j])

        return list(result)            
 
        
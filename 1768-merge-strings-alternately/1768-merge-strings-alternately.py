class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        result = []
        i = j = 0
        w1 = len(word1)
        w2 = len(word2)

        while i < w1 and j < w2:
            result.append(word1[i])
            result.append(word2[j])

            i += 1
            j += 1

        result.append(word1[i:])
        result.append(word2[j:])

        return ''.join(result)   

        
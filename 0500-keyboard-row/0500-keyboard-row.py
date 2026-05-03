class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        first_row = set('qwertyuiop')
        second_row = set('asdfghjkl')
        third_row = set('zxcvbnm')

        result = []

        for word in words:
            w = set(word.lower())

            if w.issubset(first_row) or w.issubset(second_row) or w.issubset(third_row):
                result.append(word)
                
        return result        
        
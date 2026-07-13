class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        freq1 = Counter(words1)
        freq2 = Counter(words2)

        count = 0

        for word in words1:
            if freq1[word] == 1 and freq2.get(word, 0) == 1:
                count += 1
        return count        
class Solution:
    def sortVowels(self, s: str) -> str:

        vowels = set('aeiouAEIOU')
        extractedVowels = [ch for ch in s if ch in vowels]
        extractedVowels.sort()

        result = []
        vowelIndex = 0

        for ch in s:
            if ch in vowels:
                result.append(extractedVowels[vowelIndex])
                vowelIndex += 1
            else:
                result.append(ch)

        return ''.join(result)            
        
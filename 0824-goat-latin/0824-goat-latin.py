class Solution:
    def toGoatLatin(self, sentence: str) -> str:

        words = sentence.split()
        vowels = 'aeiouAEIOU'
        result = []

        for i, word in enumerate(words):
            if word[0] in vowels:
                result.append(word + 'ma' + 'a' * (i + 1))
            else:
                result.append(word[1:] + word[0] + 'ma' + 'a' * (i + 1))

        return ' '.join(result)            





        
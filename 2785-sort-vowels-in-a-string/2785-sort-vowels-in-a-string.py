class Solution(object):
    def sortVowels(self, s):

        arr = []
        result = []
        vowelSet = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        for ch in s:
            if ch in vowelSet:
                arr.append(ch)

        arr.sort()
        i = 0

        for ch in s:
            if ch in vowelSet:
                result.append(arr[i])
                i += 1
            else:
                result.append(ch)

        return ''.join(result)            

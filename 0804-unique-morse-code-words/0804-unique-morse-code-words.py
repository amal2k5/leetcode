class Solution(object):
    def uniqueMorseRepresentations(self, words):

        result = set()
        morse =  {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}

        for word in words:
            morseCode = ''

            for m in word:
                morseCode += morse[m]
            result.add(morseCode)

        return len(result)        


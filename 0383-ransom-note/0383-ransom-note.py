class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        mag_count = {}

        for ch in magazine:
            mag_count[ch] = mag_count.get(ch, 0) + 1

        for ch2 in ransomNote:
            if mag_count.get(ch2, 0) == 0:
                return False
            mag_count[ch2] -= 1 
        return True            
        
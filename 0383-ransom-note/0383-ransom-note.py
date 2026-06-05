class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        mag_count = {}

        for ch1 in magazine:
            mag_count[ch1] = mag_count.get(ch1, 0) + 1

        for ch2 in ransomNote:
            if mag_count.get(ch2, 0) == 0:
                return False
            mag_count[ch2] -= 1 

        return True            
        
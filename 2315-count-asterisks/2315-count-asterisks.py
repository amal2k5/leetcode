class Solution:
    def countAsterisks(self, s: str) -> int:

        count = 0
        flag = False

        for ch in s:
            if ch == '|':
                flag = not flag
            elif ch == '*' and not flag:
                count += 1
        return count            
        
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        for ch in ransomNote:
            if count[ch] > 0:
                count[ch] -= 1
            else:
                return False
        return True
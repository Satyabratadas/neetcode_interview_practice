class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        for i in range(len(s)):
            if i == len(s) - 1:
                return len(s[i])
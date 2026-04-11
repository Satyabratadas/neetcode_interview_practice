class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        size = len(s)
        for i in range(size):
            if i == size - 1:
                return len(s[i])
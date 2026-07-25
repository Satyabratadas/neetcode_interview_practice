class Solution:
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
       

    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left+1, right) or self.isPalindrome(s, left, right-1)
            left, right = left + 1, right - 1
        return True

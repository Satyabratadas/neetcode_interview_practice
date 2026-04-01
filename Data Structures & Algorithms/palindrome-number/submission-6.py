class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        return x > 0 or original == rev